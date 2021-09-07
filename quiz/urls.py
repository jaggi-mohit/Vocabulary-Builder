from django.urls import path
from . import views

urlpatterns = [
    
    path('welcome',views.welcome,name='welcome'),
    path('quiz/',views.quiz,name='quiz'),
    path('result/',views.result,name='result'),
    path('saveans/',views.saveans,name='saveans'),
    path('showAnswers/',views.showAnswers,name='showAnswers')
]
    

