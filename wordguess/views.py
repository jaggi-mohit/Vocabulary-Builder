from django.shortcuts import render,redirect
import random
from django.http import HttpResponseRedirect
#from pygame import mixer
#import pygame


answer_arr=[]
answer=["PYTHON","MOBILE","ACCUSE","ABSORB","CONVINCE","MANIPULATE","EXTRACT","EVALUATE","ADEQUATE","EXAGGERATION","BIGOT"]
msg= ""
msg1=""

def rword():
    global jword
    global word
    global msg1
    word=random.choice(answer)
    
    jum= random.sample(word, len(word))
    jword = "".join(jum)
    if word == "PYTHON":
        msg1 = "This is name of famous programming language and a snake !"
    if word == "MOBILE":
        msg1 = "I am device which never leaves you alone"
    if word == "ACCUSE":
        msg1 = "To say that somebody has done something wrong or broken the law"
    if word == "ABSORB":
        msg1 = "To take in and hold something (a liquid, heat, etc.)"
    if word == "CONVINCE":
        msg1 ="To succeed in making somebody believe something"
    if word == "MANIPULATE":
        msg1 ="To influence somebody so that he/she does or thinks what you want"
    if word == "BIGOT":
        msg1 ="A person with very strong, unreasonable beliefs or opinions and who will not listen to or accept a different opinion"
    if word == "EXAGGERATION":
        msg1 ="The fact of making something seem larger, more important, better, or worse than it really is"
    if word == "ADEQUATE":
        msg1 ="Enough for what you need"
    if word =="EVALUATE":
        msg1 ="To study the facts and then form an opinion about something"
    if word =="EXTRACT":
        msg1 ="To take something out, especially with difficulty"
def guess(request):
    #mixer.init()
    #mixer.music.load(r"C:\Users\KUNAL SINGH JAGGI\Downloads\Music\game.mp3")
    #mixer.music.play()
    global chances , msg1
    chances=3
    rword()
    global jword,msg
    
    return render(request,"guess.html",{'jum_word':jword,'msg1':msg1})

def sorry(request):
    #from pygame import mixer
    #mixer.music.pause()
    return render(request,"sorry.html")

def checkans(request):
    global word , jword , msg , msg1
    msg2=""
    global chances
    x = request.GET['answer']
    y = x.upper()
    
    if y != word: 
        if y !="":  
            msg ="Sorry Your Answer Is Wrong"
            chances = chances - 1
            msg2 ="You are Left with "+ str(chances) + " chance"
            if chances ==0:
                return redirect('http://127.0.0.1:8000/sorry.html')
                 
                
    if y == word:
        msg = "That was Correct One!"
        guess(request)
        

    if y == "":
        msg ="Please Type Your Answer!"
        
    
    
    
    

                
               
                    
   
        
    return render(request,"guess.html",{'jum_word':jword,"msg":msg,'msg1':msg1,'msg2':msg2})

