from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .form import ItemForm

class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
    template_name = 'menus/form.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Items'
        return context

class ItemUpdateView(UpdateView):
    template_name = 'menus/form.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemUpdateView,self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Items'
        return context
