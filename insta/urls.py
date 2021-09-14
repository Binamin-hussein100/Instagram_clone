from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('profile',views.get_profile,name = 'profile')
]
