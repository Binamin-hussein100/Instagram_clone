from django.urls import path,re_path
from . import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('search/',views.search, name='search'),
    path('profile/',views.get_profile,name = 'profile'),
    path('register/',views.register, name='register'),
    path('',views.login, name='login'),
    path('logout',views.logout_view, name='logout')
]
