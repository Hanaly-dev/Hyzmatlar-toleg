from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', biz_barada, name='about'),
    path('hyzmatlar/', hyzmatlar, name='hyzmatlar'),
    path('login/', loginView, name='login'),
    path('logout/',logoutView, name='logout'),
    path('register/', registerView, name='register'),
    path('contact/', habarlasmak, name='contact'),
    path('toleglerim/', tolegler, name='tolegler'),
    path('toleg-etmek/', toleg_etmek, name='toleg-etmek'),
    path('profil/', profil_view, name='profil'), 
    path('hasabatlar/', hasabatlar_view, name='hasabatlar'),  
]
