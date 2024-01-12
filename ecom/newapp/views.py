from django.http import HttpResponse
import logging

# Получение экземпляра логгера
logger = logging.getLogger(__name__)


def home(request):
    # HTML-вёрстка для главной страницы
    html_content = """
        <h1>Добро пожаловать в наш интернет-магазин!</h1>
        <p>У нас вы найдете лучшие товары по выгодным ценам.</p>
        <p>Будем рады сотрудничеству!</p>
        <!-- Дополнительные блоки с товарами, акциями и другими элементами магазина -->
    """

    # Логирование посещения страницы
    logger.info("home get request")

    return HttpResponse(html_content)


def about(request):
    # HTML-вёрстка для страницы "о нас"
    html_content = """
        <h1>О нас</h1>
        <p>Мы - команда энтузиастов, с любовью к качественным товарам и удобству покупок.</p>
        <p>Наша цель - предоставить вам лучший выбор и сервис.</p>
        <!-- Информация о команде, миссии магазина и другие детали -->
    """

    # Логирование посещения страницы
    logger.info("about get request")

    return HttpResponse(html_content)
