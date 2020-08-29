from django.contrib.auth import get_user_model

User = get_user_model()

lastUserfromDb = User.objects.last()

#my followers
lastUserfromDb.profile.followers.all()

#who I follow
lastUserfromDb.is_following.all() #== lastUserfromDb.profile.following.all()
