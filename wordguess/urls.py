from django.urls import path
from . import views

urlpatterns = [
    
    path('guess/',views.guess,name='guess'),
    path('guess/checkans',views.checkans,name='checkans'),
    path('sorry.html',views.sorry,name='sorry')
]