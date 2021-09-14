from django.shortcuts import render
from insta.models import Profile,Posts,Comments,Followers
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = Posts.objects.all()
    return render(request,'instagram.html',{"posts":posts})

def get_profile(request):
    prof = Profile.objects.all()
    return render(request,'insta_profile.html',{"prof":prof})