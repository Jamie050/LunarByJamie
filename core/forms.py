from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.forms import ModelForm
from .models import User,UserProfile,Post

class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label =  ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Verify Password'

        
    class Meta:
        model = User
        fields = ['username','password1','password2']


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label =  ''
        self.fields['password'].label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'password'

    class Meta:
        model = User




class ProfileForm(ModelForm):


    class Meta:
        model = UserProfile
        fields = ['avatar','bio']



class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].label = ''
        self.fields['content'].label = ''
        self.fields['thumbnail'].label = ''

        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['content'].widget.attrs['placeholder'] = 'Blah Blah Blah .....'


    class Meta:
        model = Post
        fields = ['subject','content','thumbnail']

    