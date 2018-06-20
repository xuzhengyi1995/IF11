from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
import os
import json
import hashlib
import sys
sys.path.append(r'./main/')
from main.music_prosecess import musicProcessor

mp = musicProcessor()

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

def uploadMusic(request):
    m_file = request.FILES['music']
    song_name = request.POST['song_name']
    exts = str(m_file).split(".")
    ext = exts[len(exts)-1]
    fhash = hashlib.sha1(m_file.read()).hexdigest()
    fname = 'music_uploaded/'+str(fhash)+'.'+str(ext)
    res = {}
    if(not os.path.isfile(fname)):
        with open(fname, 'wb') as f:
            for chunk in m_file.chunks():
                f.write(chunk)
        reg_res = mp.reg_file(fname)
        print(reg_res)
        if((not reg_res) or reg_res["confidence"]<25):
            res = {"error":False, "error_type":"", "message":"Upload ok"}
            mp.fp_file(fname, song_name)
        else:
            res = {"error":True, "error_type":"FIND_SAME_FINGERPRINT_MUSIC", "message":reg_res}
    else:
        res = {"error":True, "error_type":"SAME_FILE"}
    return HttpResponse(json.dumps(res), content_type="application/json")
