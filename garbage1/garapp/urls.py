from django.urls import path
from . import views
urlpatterns = [
    path('',views.login1),
    path('reg1',views.reg1,name='reg1'),
    path('register',views.register),
    path('login',views.login,name='login')
    

]
