from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.http import Http404
from schools.models import School
from menus.models import Item

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
        owner = self.get_object()
        name = owner.username
        query = self.request.GET.get('searchText')
        qs = School.objects.filter(owner=owner).search(query.strip()) # strip function remove the void space from left and right.
        # item_exists = Item.objects.filter(user=owner).exists()
        context['title'] = f'{name}'
        # if query:
        #     # qs = School.objects.search(query)
        #     qs = qs.search(query)
        if qs.exists():
            context['schools'] = qs
        return context
