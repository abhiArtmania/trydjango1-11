from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Display simple string
def home(request):
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
