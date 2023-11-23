from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from products import views
urlpatterns = [
    path('',views.home,name='home'),
    path('productdetails/<str:slug>',views.productdetails,name='productdetails'),
    path('categorydetails/<str:slug>',views.categorydetails,name='categorydetails'),
    path('searchitem',views.searchitem,name='searchitem'),
    path('shoppingcart/<str:slug>',views.shoppingcart,name='shoppingcart')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)