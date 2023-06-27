from django.urls import path
from .views import index, register, gallery, cafe, aboutus, faq
urlpatterns = [
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('cafe/', cafe, name='cafe'),
    path('aboutus/', aboutus, name='aboutus'),
    path('faq/', faq, name='faq'),
    path('register/', register, name='register'),
]