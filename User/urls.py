from django.contrib import admin
from django.urls import path,include
from User import views
from django.contrib.auth.views import LogoutView
from .views import UserLogin

from .views import Createuser,Deleteuser,Updateuser,UserDetail
app_name='user_urls'


urlpatterns = [
    path('create/',Createuser.as_view()),
    path('<pk>/delete/',Deleteuser.as_view()),
    path('<pk>/update/',Updateuser.as_view()),
    path('<pk>/detail/',UserDetail.as_view()),
    path('index/',views.index),
    path('register/',views.register),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='User/user_login.html'), name='logout'),

]