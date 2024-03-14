

from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.CreatecompanyNew, name='homepage'),
    path('signin/', views.CreatecompanyNew, name='signinpage'),
    path('signup/', views.CreatecompanyNew, name='signuppage'),
    path('1st/', views.CreatecompanyNew, name='firstpage')

]