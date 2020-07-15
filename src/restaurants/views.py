from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
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


    # # Display simple string
    # def string(request):
    #     return HttpResponse('Hello')
    #
    # # Display simple html
    # def simpleHtml(request):
    #     html = """<html lang=en>
    #     <head>
    #     <body>
    #     <h1>Hello World!</h1>
    #     <p>This is simple HTML page.</p>
    #     </body>
    #     </head>
    #     </html>
    #     """
    #     return HttpResponse(html)
    #
    # # Python 3.6 have a feature of string substitution
    # def stringSubtution(request):
    #     htmlVar = 'string substitution'
    #     html = f"""<html lang=en>
    #     <head>
    #     <body>
    #     <h1>Hello World!</h1>
    #     <p>This is the example of {htmlVar}</p>
    #     </body>
    #     </head>
    #     </html>
    #     """
    #     return HttpResponse(html)
    #
    # def home(request):

    #     return render(request,'home.html',context)
    #     # render(request,templatename,pythonDictionary)
    #
    # def about(request):
    #     return render(request,'about.html',{})
    #
    # # Normal render of django template
    # def contact(request):
    #     return render(request,'contact.html',{})
    #
    # # Class based views
    # class ContactView(View):
    #     def get(self, request, *args, **kwargs):
    #         context = {}
    #         return render(request, 'contact.html', context)
    #
    # # Template View
    # #class ContactTemplateView(TemplateView):
    # #    template_name = 'contact.html'
