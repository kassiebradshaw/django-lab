from django.urls.resolvers import URLPattern
from django.urls import path
from .views import SecondHome

urlpatterns = [
    path('', SecondHome.as_view(), name='secondhome'),
]