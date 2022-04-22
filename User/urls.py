from django.contrib import admin
from django.urls import path,include
from User import views
from django.contrib.auth.views import LogoutView
from .views import UserLogin,SignUpView
from .views import Createuser,Deleteuser,Updateuser,UserDetail
app_name='user_urls'


urlpatterns = [
    path('create/',Createuser.as_view()),
    path('<pk>/delete/',Deleteuser.as_view()),
    path('<pk>/update/',Updateuser.as_view()),
    path('<pk>/detail/',UserDetail.as_view()),
    path('',views.index),
    path('contact/',views.contact,name='contact'),
    path('categories/',views.categories,name='categories'),
    path('listing/',views.listing,name='listing'),
    path('register/',SignUpView.as_view(),name='register'),
    path('login/',UserLogin.as_view(), name='login'),
    

]