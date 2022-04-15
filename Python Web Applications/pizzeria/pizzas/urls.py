# Defines URL patterns for pizzas

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
	# Home page:
	path('', views.index, name='index'),
	# Page for displaying available pizzas:
	path('menu/', views.menu, name='menu'),
	# Page for the ingredients of chosen pizza:
	path('menu/<int:menuitem_id>/', views.menuitem, name='menuitem'),
]
