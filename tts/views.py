from django.shortcuts import render, redirect
import pyttsx3
from django.http import HttpResponseRedirect



def speech(request):
    return render(request,'speech.html')


    
def speech1(request):
    
    txt = request.GET['inp']
    engine = pyttsx3.init()
    engine. setProperty("rate", 180)
    engine.say(txt)
    engine.runAndWait()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

   
    
