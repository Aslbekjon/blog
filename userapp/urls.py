from django.urls import path
from .views import *

urlpatterns = [
    path('', Users.as_view(), name='users'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('user_detail/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('profile_update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile_delete/', ProfileDelete.as_view(), name='profile_delete'),
]