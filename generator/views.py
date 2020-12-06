from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')


def password(request):

    character = list('abcdefghijklmnoprstuvwxyz')
    
    length = int(request.GET.get ('lenght', 6)) 

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) 

    if request.GET.get("numbers"):
        character.extend(list(1234567890))

    if request.GET.get("special character"):
        character.extend(list('~!@#$%^&'))
        

    thepassword = ""

    for x in range(length):

        thepassword += random.choice(character)
    

    return render(request,'generator/password.html', {'password':thepassword})

def about(request):
        return render(request, 'generator/about.html')
        





