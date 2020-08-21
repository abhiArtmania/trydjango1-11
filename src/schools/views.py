from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import School
from .form import SchoolCreateForm
from django.contrib.auth import logout
import random

# Create your views here.

# Home view
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        num = random.randint(0,1000)
        context = {
            "UserExist":True,
            "username":'Abhishek Singh',
            'age':num,
            'familyMembers':['Ashish','Shashikala','Ashok']
        }
        return context

# About view
class AboutView(TemplateView):
    template_name = 'about.html'

# Contact view
class ContactView(TemplateView):
    template_name = 'contact.html'

# def school_list(request):
#     template_name = '/schools/school_list.html'
#     queryset = School.objects.all()
#     context = {
#         "school":queryset
#     }
#     return render(request,template_name,context)

# class SchoolListView(ListView):
#     model = School
#     template_name = 'school_list.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(SchoolListView,self).get_context_data(*args,**kwargs)
#         queryset = School.objects.all()
#         context['school'] = queryset
#         return context

class SearchSchoolListView(LoginRequiredMixin, ListView):
    model = School
    def get_context_data(self,*args, **kwargs):
        queryset = School.objects.filter(owner=self.request.user)
        context = super(SearchSchoolListView,self).get_context_data(*args, **kwargs)
        context['school'] = queryset
        return context

class SearchSchoolDetailView(LoginRequiredMixin, DetailView):
    model = School
    def get_context_data(self,*args, **kwargs):
        queryset = School.objects.filter(owner=self.request.user)
        context = super(SearchSchoolDetailView,self).get_context_data(*args,**kwargs)
        context['school']=queryset
        return context
    # def get_context_data(self, *args, **kwargs):
    #     context = super(SearchSchoolDetailView,self).get_context_data(*args, **kwargs)
    #     return context

    # change the default object - pk/slug to your custom object name.
    # here my custom object name = school_id
    # def get_object(self,*args,**kwargs):
    #     school_id = self.kwargs['school_id']
    #     obj = get_object_or_404(School, pk=school_id) #pk = school_id
    #     return obj


# School create view in containing too many lines (function based view)
# def School_createView(request):
#     form = SchoolCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         if request.user.is_authenticated():
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#             # Like a post_save
#             return HttpResponseRedirect('/school/')
#         else:
#             return HttpResponseRedirect('/login/')
#     if form.errors:
#         errors = form.errors
#     template_name = 'schools/form.html'
#     context = {"form":form, "errors":errors}
#     return render(request, template_name, context)

# School create view in les number of lines (class based view)
class School_createView(LoginRequiredMixin,CreateView):
    login_url = '/login/'                                  # You can also set the default login url in local.py
    template_name = 'schools/form.html'
    form_class = SchoolCreateForm

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(School_createView,self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(School_createView,self).get_context_data(*args, **kwargs)
        context['title'] = 'Add School'
        return context

class School_updateView(LoginRequiredMixin,UpdateView):
    model = School
    login_url = '/login/'                                  # You can also set the default login url in local.py
    template_name = 'schools/detail-update.html'
    form_class = SchoolCreateForm

    def get_context_data(self,*args,**kwargs):
        context = super(School_updateView,self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f'Update School: {name}'
        return context

class LogoutUser(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,*args,**kwargs):
        logout(self.request)
