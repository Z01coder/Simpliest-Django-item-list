from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу
            return redirect('film_list')  # После успешного сохранения перенаправляем
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def film_list(request):
    films = Film.objects.all()  # Получаем все фильмы из базы
    return render(request, 'films/film_list.html', {'films': films})
