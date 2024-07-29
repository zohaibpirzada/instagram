from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Email', 'class' : 'form-control', "id" : 'email'}))
    class Meta:
        model = User
        fields = ['username','email', "password1", 'password2']
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
        self.fields['username'].help_text = "<span class='form-text'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>"
    
    
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Your Password'
        self.fields['password1'].help_text = '''
        <ul class='form-text'>
            <li>Your password can’t be too similar to your other personal information.</li>
            <li>Your password must contain at least 8 characters.</li>
            <li>Your password can’t be a commonly used password.</li>
            <li>Your password can’t be entirely numeric.</li>
        </ul>'''


        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Conform Password'
        self.fields['password2'].help_text = "<span class='form-text'> Enter the same password as before, for verification.</span>"

class UserProfileEditForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Email', 'class' : 'form-control', "id" : 'email'}))

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'First Name', 'class' : 'form-control', "id" : 'fname', "aria-label":"First name"}))
    
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Last Name', 'class' : 'form-control', "id" : 'lname', "aria-label":"Last name"}))

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = "<span class='form-text'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>"


class ProfileImagePic(forms.ModelForm):
    profile_image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class' : 'form-control', 'id' : 'image'}))
    
    user_bio = forms.CharField(label='', widget=forms.Textarea(attrs={'class' : 'form-control', 'id' : 'bio', 'placeholder' : 'Bio'}), max_length=200)
    
    user_website = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'website', 'placeholder' : 'Website'}), max_length=200)

    user_facebook = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'facebook', 'placeholder' : 'FaceBook'}), max_length=200)

    user_instagram = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'instagram', 'placeholder' : 'Instagram'}), max_length=200)
    class Meta:
        model = Profile
        fields = ['profile_image', "user_bio",'user_website', 'user_instagram', 'user_facebook']

class CreatePost(forms.ModelForm):
    Title = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'id' : 'title', 'placeholder' : 'Post Title..'}), max_length=200)

    body = forms.CharField(required=True,widget=forms.widgets.Textarea(attrs={'placeholder':'Post...', "class" : "form-control", 'id' : 'post_body'}), label = '')
    post_image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class' : 'form-control', 'id' : 'image'}))
    
    POST_STATUS = (
        ('Public' , 'Public'),
        ('Private' , 'Private'),
    )

    post_status = forms.CharField(label='', widget=forms.Select(choices=POST_STATUS, attrs={'class' : "form-select", 'id' : 'post_status'}), max_length=20)

    class Meta:
        model = UserPost
        fields = ['Title','body', 'post_image', 'post_status' ]        


class Post_comment_form(forms.ModelForm):
    body = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={ 'placeholder':'Comment...', "class" : "form-control", 'id' : 'post_body'}), label = '')
    class Meta:
        model = Post_comment
        exclude = ['user', 'post',]