from  django import forms
from insta.models import Posts,Profile
from cloudinary.models import CloudinaryField


class NewpostForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        exclude = ['user', 'profile','likes']
        fields = ['image','title','caption',]
        
class Editprofileform(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        fields = ['location','photo','bio']