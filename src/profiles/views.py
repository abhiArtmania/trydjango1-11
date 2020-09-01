from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, CreateView
from django.contrib.auth import get_user_model
from django.http import Http404
from schools.models import School
from menus.models import Item
from .models import Profile
from .forms import RegisterForm

User = get_user_model()

class RegisterForm(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/login/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect("/logout/")
        return super(RegisterForm,self).dispatch(*args, **kwargs)

class ProfileFollowUnfollow(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        user_to_follow_unfollow = request.POST.get("username")
        profile_, is_following = Profile.objects.follow_unfollow(request.user, user_to_follow_unfollow)
        # profile_ = Profile.objects.get(user__username__iexact=user_to_follow_unfollow)
        # logggedIn_user = request.user
        # if logggedIn_user in profile_.followers.all():
        #     profile_.followers.remove(logggedIn_user)
        # else:
        #     profile_.followers.add(logggedIn_user)
        # return redirect(f"/profile/{user_to_follow_unfollow}/")
        return redirect(f"/profile/{profile_.user.username}/")

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'
    def get_object(self):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User,username__iexact=username, is_active=True)

    def get_context_data(self,*args,**kwargs):
        context = super(ProfileDetailView,self).get_context_data(*args,**kwargs)
        owner = self.get_object()
        is_following = False
        if owner.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        name = owner.username
        query = self.request.GET.get('searchText')
        qs = School.objects.filter(owner=owner).search(query) # strip function remove the void space from left and right.
        # item_exists = Item.objects.filter(user=owner).exists()
        context['title'] = f'{name}'
        # if query:
        #     # qs = School.objects.search(query)
        #     qs = qs.search(query)
        if qs.exists():
            context['schools'] = qs
        return context
