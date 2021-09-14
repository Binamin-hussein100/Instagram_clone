from insta.models import Comments, Followers, Posts, Profile
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Followers)
admin.site.register(Comments)
