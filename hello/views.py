from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse('Hello!')
    return render(request, 'hello/index.html')

def brian(request):
    return HttpResponse('Hello Brian')

def joyline(request):
    return HttpResponse('Hello Joyline')
def greet(request, name):
    # return HttpResponse(f'Hello, {name.capitalize()}!')
    return render(request, 'hello/greet.html', {
        'name':name.capitalize()
    })