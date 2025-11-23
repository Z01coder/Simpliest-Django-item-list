from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
import re

class Film(models.Model):
    """Модель фильма с валидацией на уровне модели."""
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Описание фильма", blank=True)
    review = models.TextField(verbose_name="Отзыв", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['title']

    def clean(self):
        """Валидация на уровне модели."""
        super().clean()
        
        # Валидация названия
        if self.title:
            title = strip_tags(self.title)
            if len(title.strip()) < 2:
                raise ValidationError({'title': 'Название фильма должно содержать минимум 2 символа.'})
            if re.search(r'<script|javascript:|onerror=|onload=', title, re.IGNORECASE):
                raise ValidationError({'title': 'Название содержит недопустимые символы.'})
        
        # Валидация описания
        if self.description:
            description = strip_tags(self.description)
            if len(description) > 5000:
                raise ValidationError({'description': 'Описание не должно превышать 5000 символов.'})
            if re.search(r'<script|javascript:|onerror=|onload=', description, re.IGNORECASE):
                raise ValidationError({'description': 'Описание содержит недопустимые символы.'})
        
        # Валидация отзыва
        if self.review:
            review = strip_tags(self.review)
            if len(review) > 5000:
                raise ValidationError({'review': 'Отзыв не должен превышать 5000 символов.'})
            if re.search(r'<script|javascript:|onerror=|onload=', review, re.IGNORECASE):
                raise ValidationError({'review': 'Отзыв содержит недопустимые символы.'})

    def save(self, *args, **kwargs):
        """Переопределяем save для вызова clean."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
