from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Item
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from .form import ItemForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "home.html", {})

        user = request.user
        is_following_user_ids = [f_user.user.id for f_user in user.is_following.all()]
        print(is_following_user_ids)
        # following is this simillar code for looping
        # list_
        # for f_user in user.is_following.all():
        #   list_.append(f_user.user.id)

        qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True)#.order_by("-updatedAt")][:3]

        return render(request, "menus/home-feed.html", {'object_list':qs})

class ItemListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'menus/form.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Items'
        return context

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'menus/detail-update.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemUpdateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Items'
        return context
