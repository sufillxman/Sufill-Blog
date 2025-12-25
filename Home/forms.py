from django import forms
from .models import BlogModel
from froala_editor.widgets import FroalaEditor

class blogform(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content', 'image'] # Title aur Image bhi yahan add kar diye
        
        # Bootstrap styling yahi de dete hain taaki HTML ganda na ho
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title'}),
            'content': FroalaEditor(),
        }