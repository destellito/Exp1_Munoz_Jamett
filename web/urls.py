from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, register, gallery, cafe, aboutus, faq, product_list, agregar, agregarrec, eliminar, actualizar, actualizarrec, carrito, eliminar_del_carrito, finalizar_compra, GalleryView
urlpatterns = [
    path('', index, name='index'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
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
    path('carrito/', carrito, name='carrito'),
    path('eliminar_del_carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)