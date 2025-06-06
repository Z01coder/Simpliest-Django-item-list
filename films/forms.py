from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название фильма'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание фильма'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш отзыв'}),
        }
