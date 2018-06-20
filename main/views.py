from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
import os

def home(request):
    return render(request, 'index.html')

def signIn(request):
    return render(request, 'signin.html')

def signUp(request):
    return render(request, 'signup.html')

def tianDi(request):
    return render(request, 'tiandi.html')

def redirectToImages(request, item):
    return HttpResponsePermanentRedirect("/static/images/" + item)

def redirectToJs(request, item):
    return HttpResponsePermanentRedirect("/static/js/" + item)

def redirectToJsFolder(request, folder, item):
    return HttpResponsePermanentRedirect(os.path.join("/static/js/", folder, item))

def redirectToJsFolder2(request, folder, folder2, item):
    return HttpResponsePermanentRedirect(os.path.join("/static/js/", folder, folder2, item))

def redirectToCss(request, item):
    return HttpResponsePermanentRedirect("/static/css/" + item)

def redirectToFonts(request, item):
    return HttpResponsePermanentRedirect("/static/fonts/" + item)

def redirectToFonts2(request, folder, item):
    return HttpResponsePermanentRedirect(os.path.join("/static/fonts/", folder, item))

def returnProfile(request):
    return render(request, 'profile.html')
