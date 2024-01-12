from django.http import HttpResponse
import logging

# Получение экземпляра логгера
logger = logging.getLogger(__name__)


def home(request):
    # HTML-вёрстка для главной страницы
    html_content = """
        <h1>Главная страница Django-сайта.</h1>
        <p>Рады видеть Вас в нашем интернет-магазине</p>
    """

    # Логирование посещения страницы
    logger.info("home get request")

    return HttpResponse(html_content)


def about(request):
    # HTML-вёрстка для страницы "о нас"
    html_content = """
        <h1>О нас</h1>
        <p>Привет! Меня зовут Django и это мой интернет-магазине.</p>
    """

    # Логирование посещения страницы
    logger.info("about get request")

    return HttpResponse(html_content)
