from django.urls import path
from . import views
from quiz import views as cv
from tts import views as vs
from wordguess import views as ws

urlpatterns = [
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
    path('welcome',cv.welcome,name='welcome'),
    path('quiz/',cv.quiz,name='quiz'),
    path('result/',cv.result,name='result'),
    path('saveans/',cv.saveans,name='saveans'),
    path('showAnswers/',cv.showAnswers,name='showAnswers'),
    path('speech/',vs.speech,name='speech'),
    path('speech/speech1',vs.speech1,name='speech1'),
    path('guess/',ws.guess,name='guess'),
    path('guess/checkans',ws.checkans,name='checkans'),
    path('sorry.html',ws.sorry,name='sorry')
   

    
]

   




