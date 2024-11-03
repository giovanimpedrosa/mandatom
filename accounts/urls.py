from django.urls import path
from accounts.views import logar_view


urlpatterns = [
    path('logar/', logar_view, name='logar')
]