from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'
    def get_object(self):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User,username__iexact=username, is_active=True)

    def get_context_data(self,*args,**kwargs):
        context = super(ProfileDetailView,self).get_context_data(*args,**kwargs)
        name = self.get_object().username
        context['title'] = f'{name}'
        return context
