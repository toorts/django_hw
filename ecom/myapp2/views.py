from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from datetime import timedelta

from .models import User, Order, Product
from .forms import ImageForm


def ordered_products(request, user_id):
    user = User.objects.get(id=user_id)
    orders = Order.objects.filter(user=user)

    # Функция для получения товаров за указанный период
    def get_ordered_products(period):
        start_date = timezone.now() - timedelta(days=period)
        ordered_products = Product.objects.filter(
            order__in=orders, order__order_date__gte=start_date).distinct()
        return ordered_products

    # Получаем списки товаров для каждого периода
    products_last_week = get_ordered_products(7)
    products_last_month = get_ordered_products(30)
    products_last_year = get_ordered_products(365)

    context = {
        'user': user,
        'products_last_week': products_last_week,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year,
    }

    return render(request, 'myapp2/ordered_products.html', context)


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp2/upload_image.html', {'form': form})