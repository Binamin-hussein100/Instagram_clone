from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save


# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    photo = CloudinaryField('image')
    bio = models.TextField(max_length=350, default="Hello their am using instagram_clone", blank=True)

    def save_profile(self):
        self.save()
        

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

    @classmethod
    def search_profile(cls,name):
        profile = cls.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_profile(cls,id):
        profile = cls.objects.get(id = id)
        return profile

def user_profile(sender,**kwargs):
    if kwargs['created']:
        prof = Profile.objects.create(user=kwargs['instance'])

post_save.connect(user_profile, sender=User)

class Posts(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE,default=None)
    image = CloudinaryField('image')
    title = models.CharField(max_length=30)
    caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=CASCADE)
    likes = models.IntegerField(default=None)
    
    class Meta:
        ordering = ['-pk']
        verbose_name_plural = 'Images'
        
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    def __str__(self):
        return self.title
    
    
class Followers(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    
    class Meta:
            ordering = ['-pk']
            verbose_name_plural = 'followers'
    
    def __str__(self):
        return self.follower
    
class Comments(models.Model):
    comment = models.CharField(max_length=300)
    
    class Meta:
            ordering = ['-pk']
            verbose_name_plural = 'comments'
    
    def __str__(self):
        return self.comment
    