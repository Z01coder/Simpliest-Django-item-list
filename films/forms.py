from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
import re
from .models import Film

class FilmForm(forms.ModelForm):
    """Форма для добавления фильма с валидацией данных."""
    
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название фильма'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание фильма', 'rows': 4}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш отзыв', 'rows': 4}),
        }
    
    def clean_title(self):
        """Валидация названия фильма."""
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Название фильма обязательно для заполнения.')
        
        # Удаляем HTML теги
        title = strip_tags(title)
        
        # Проверка на минимальную длину
        if len(title.strip()) < 2:
            raise ValidationError('Название фильма должно содержать минимум 2 символа.')
        
        # Проверка на максимальную длину
        if len(title) > 200:
            raise ValidationError('Название фильма не должно превышать 200 символов.')
        
        # Проверка на опасные символы (скрипты)
        if re.search(r'<script|javascript:|onerror=|onload=', title, re.IGNORECASE):
            raise ValidationError('Название содержит недопустимые символы.')
        
        return title.strip()
    
    def clean_description(self):
        """Валидация описания фильма."""
        description = self.cleaned_data.get('description')
        if description:
            # Удаляем HTML теги
            description = strip_tags(description)
            
            # Проверка на максимальную длину
            if len(description) > 5000:
                raise ValidationError('Описание не должно превышать 5000 символов.')
            
            # Проверка на опасные символы
            if re.search(r'<script|javascript:|onerror=|onload=', description, re.IGNORECASE):
                raise ValidationError('Описание содержит недопустимые символы.')
        
        return description.strip() if description else description
    
    def clean_review(self):
        """Валидация отзыва."""
        review = self.cleaned_data.get('review')
        if review:
            # Удаляем HTML теги
            review = strip_tags(review)
            
            # Проверка на максимальную длину
            if len(review) > 5000:
                raise ValidationError('Отзыв не должен превышать 5000 символов.')
            
            # Проверка на опасные символы
            if re.search(r'<script|javascript:|onerror=|onload=', review, re.IGNORECASE):
                raise ValidationError('Отзыв содержит недопустимые символы.')
        
        return review.strip() if review else review
