from django.urls import path
from . import views

urlpatterns = [
    
    path('speech/',views.speech,name='speech'),
    path('speech/speech1',views.speech1,name='speech1')
    
]
    