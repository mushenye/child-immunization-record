from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User  

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1','password2')  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', )  # Customize fields as necessary

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: further customization for the change form fields
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
