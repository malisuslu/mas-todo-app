from .models import TodoItem
from django import forms

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
