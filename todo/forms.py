from .models import TodoItem
from django import forms
from django.db import models
from todo.models import TodoItem, TodoUser
from django.contrib.auth.forms import UserCreationForm
class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'content', 'priority', 'is_done']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control rounded-4 resize-none', 'rows': 4, 'placeholder': 'Enter Todo content'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter a priority number'}),
            'is_done': forms.CheckboxInput(attrs={'class': ''}),
        }
    
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['content'].label = 'Content'
        self.fields['priority'].label = 'Priority'
        self.fields['is_done'].label = 'Is Done?'

    # css field classes


class UserForm(UserCreationForm):
    class Meta:
        model = TodoUser
        
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'avatar', 'page_url']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Confirm password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter last name'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter avatar'}),
            'page_url': forms.URLInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Enter page url'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['avatar'].label = 'Avatar'
        self.fields['page_url'].label = 'Page URL'

    # css field classes