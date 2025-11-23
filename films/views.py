from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django_ratelimit.decorators import ratelimit
from django_ratelimit.exceptions import Ratelimited
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_http_methods
import logging
from .forms import FilmForm
from .models import Film

logger = logging.getLogger('security')

@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def login_view(request):
    """Представление для входа пользователя с ограничением попыток."""
    if request.user.is_authenticated:
        return redirect('film_list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f'Успешный вход пользователя: {user.username} с IP: {request.META.get("REMOTE_ADDR")}')
            return redirect('film_list')
        else:
            # Логируем неудачные попытки входа
            username = request.POST.get('username', 'unknown')
            ip_address = request.META.get('REMOTE_ADDR', 'unknown')
            logger.warning(f'Неудачная попытка входа: пользователь={username}, IP={ip_address}')
    else:
        form = AuthenticationForm()
    
    # Обработка превышения лимита запросов
    if getattr(request, 'limited', False):
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')
        logger.warning(f'Превышен лимит попыток входа с IP: {ip_address}')
        messages.error(request, 'Слишком много попыток входа. Попробуйте позже.')
    
    return render(request, 'films/login.html', {'form': form})

@login_required
def logout_view(request):
    """Представление для выхода пользователя."""
    logout(request)
    return redirect('film_list')

@ratelimit(key='user', rate='10/h', method='POST', block=True)
@login_required
def add_film(request):
    """Представление для добавления фильма с ограничением частоты запросов."""
    # Обработка превышения лимита запросов
    if getattr(request, 'limited', False):
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')
        logger.warning(f'Превышен лимит добавления фильмов: пользователь={request.user.username}, IP={ip_address}')
        messages.error(request, 'Превышен лимит добавления фильмов. Попробуйте позже.')
        return redirect('film_list')
    
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()  # Сохраняем данные в базу
            logger.info(f'Фильм добавлен: {film.title} пользователем: {request.user.username}, IP: {request.META.get("REMOTE_ADDR")}')
            messages.success(request, 'Фильм успешно добавлен!')
            return redirect('film_list')  # После успешного сохранения перенаправляем
        else:
            # Логируем ошибки валидации
            ip_address = request.META.get('REMOTE_ADDR', 'unknown')
            logger.warning(f'Ошибка валидации формы добавления фильма: пользователь={request.user.username}, IP={ip_address}, ошибки={form.errors}')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def film_list(request):
    """Представление для отображения списка фильмов (доступно всем)."""
    films = Film.objects.all()  # Получаем все фильмы из базы
    return render(request, 'films/film_list.html', {'films': films})
