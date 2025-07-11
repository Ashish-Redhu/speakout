from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 1.
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'photo']  # Fields to be included in the form

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError("Content cannot exceed 240 characters.")
        return content

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo and photo.size > 5 * 1024 * 1024:  # Limit photo size to 5MB
            raise forms.ValidationError("Photo size cannot exceed 5MB.")
        return photo

# 2.   
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Fields to be included in the registration form
