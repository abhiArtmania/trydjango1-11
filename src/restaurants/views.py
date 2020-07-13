from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
# Display simple string
def string(request):
    return HttpResponse('Hello')

# Display simple html
def simpleHtml(request):
    html = """<html lang=en>
    <head>
    <body>
    <h1>Hello World!</h1>
    <p>This is simple HTML page.</p>
    </body>
    </head>
    </html>
    """
    return HttpResponse(html)

# Python 3.6 have a feature of string substitution
def stringSubtution(request):
    htmlVar = 'string substitution'
    html = f"""<html lang=en>
    <head>
    <body>
    <h1>Hello World!</h1>
    <p>This is the example of {htmlVar}</p>
    </body>
    </head>
    </html>
    """
    return HttpResponse(html)

def home(request):
    num = random.randint(0,1000)
    context = {
    "UserExist":True,
    "username":'Abhishek Singh',
    'age':num,
    'familyMembers':['Ashish','Shashikala','Ashok']
    }
    return render(request,'base.html',context)
    # render(request,templatename,pythonDictionary)
