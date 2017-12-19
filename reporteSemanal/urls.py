
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hacerReporte', views.hacerReporte, name = 'hacer_reporte'),
]