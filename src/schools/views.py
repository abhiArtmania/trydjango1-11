from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import School
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

def school_list(request):
    template_name = 'school_list.html'
    queryset = School.objects.all()
    context = {
        "school":queryset
    }
    return render(request,template_name,context)

# class SchoolListView(ListView):
#     model = School
#     template_name = 'school_list.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(SchoolListView,self).get_context_data(*args,**kwargs)
#         queryset = School.objects.all()
#         context['school'] = queryset
#         return context

class SearchSchoolListView(ListView):
    template_name = 'school_list.html'
    model = School
    def get_context_data(self,*args, **kwargs):
        print(bool(self.kwargs))
        if bool(self.kwargs):
            location = self.kwargs['location']
        else:
            location = None
        if location:
            # query to filter objects on location basis (not case-sensitive)
            queryset = School.objects.filter(location__iexact=location)
            # query to filter objects on location basis or name that contains 'Arya' character
            # queryset = School.objects.filter(
            #     Q(location__iexact=location) | Q(name__icontains='Arya')
            # )
        else:
            queryset = School.objects.all()
        context = super(SearchSchoolListView,self).get_context_data(*args, **kwargs)
        context['school'] = queryset
        return context
