from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from .utils import code_generator
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def follow_unfollow(self, request_user, user_to_follow_unfollow):
        profile_ = Profile.objects.get(user__username__iexact=user_to_follow_unfollow)
        user = request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following

class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    # following = models.ManyToManyField(User, related_name='following', blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not  self.activated:
            self.activation_key = code_generator()
            self.save()
            path_ = reverse('activate', kwargs={"code":self.activation_key})
            subject = 'Activate Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activate your account here: {path_}'
            recipient_list = [self.user.email]
            html_message = f'<p>Activate your account here: {path_}</p>'
            print(html_message)
            # sent_mail = send_mail(
            #     subject,
            #     message,
            #     from_email,
            #     recipient_list,
            #     fail_silently=False,
            #     html_message=html_message
            # )
            sent_mail = False
            return sent_mail

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        # Following two line code is for - If I create any new user then, it becomes the follower of a user profile having id = 2
        default_user_profile = Profile.objects.get_or_create(user__id=2)[0]
        default_user_profile.followers.add(instance)
        # Following two line code is for - If I create any new user then, above default user profile become follower of this new userself.
        profile.followers.add(default_user_profile.user)

post_save.connect(post_save_user_receiver, sender=User)
