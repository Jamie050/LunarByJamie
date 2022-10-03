from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.forms import ModelForm
from .models import User,UserProfile,Post

class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label =  'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password'

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
    class Meta:
        model = User
        fields = ['username','password1','password2']



class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar','bio']



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['subject','content','thumbnail']

    