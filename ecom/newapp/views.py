from django.http import HttpResponse
import logging
from django.shortcuts import render

# Получение экземпляра логгера
logger = logging.getLogger(__name__)


def home(request):
    context = {
        'title': 'Главная страница',
    }

    # Логирование посещения страницы
    logger.info("Home page accessed")

    return render(request, 'newapp/home.html', context)


def about(request):
    context = {
        'title': 'О нас',
    }

    # Логирование посещения страницы
    logger.info("About page accessed")

    return render(request, 'newapp/about.html', context)
