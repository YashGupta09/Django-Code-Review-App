from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.config, name='app_config')
]