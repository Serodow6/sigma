from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
app_name = 'accounts'
urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('user_profile/<int:id>/',user_profile,name='user_profile'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('edit_profile/<int:pk>/',EditProfile.as_view(),name='edit_profile'),
    
]