from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from social.models import UserProfile,Posts,Comments,Stories


class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=('user','following','block')
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"})
            }
        

class PostForm(forms.ModelForm):

    class Meta:
        model=Posts
        fields=["title","post_image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['text']


class StoryForm(forms.ModelForm):

    class Meta:
        model=Stories
        fields=["title","post_image"]
    