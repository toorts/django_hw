from django.urls import path

from .views import ordered_products, upload_image


urlpatterns = [
    path('ordered_products/', ordered_products, name='ordered_products'),
    path('upload/', upload_image, name='upload_image'),  # type: ignore
]
