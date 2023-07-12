from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, register, gallery, cafe, aboutus, faq, product_list, agregar, agregarrec, eliminar, actualizar, actualizarrec
urlpatterns = [
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('cafe/', cafe, name='cafe'),
    path('aboutus/', aboutus, name='aboutus'),
    path('faq/', faq, name='faq'),
    path('register/', register, name='register'),
    path('product_list/', product_list, name='product_list'),
    path('agregar/', agregar, name='agregar'),
    path('agregarrec', agregarrec, name='agregarrec'),
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    path('actualizar/<int:id>/', actualizar, name='actualizar'),
    path('actualizar/actualizarrec/<int:id>/', actualizarrec, name='actualizarrec'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)