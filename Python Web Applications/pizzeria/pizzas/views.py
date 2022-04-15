from django.shortcuts import render
from .models import Pizza

def index(request):
	"""Home page for Pepe's Pizzeria"""
	return render(request, 'pizzas/index.html')

def menu(request):
	"""Menu page:"""
	pizzas = Pizza.objects.all()
	context = {'pizzas': pizzas}
	return render(request, 'pizzas/menu.html', context)

def menuitem(request, menuitem_id):
	"""Page for ingredients of each menu item"""
	menuitem = Pizza.objects.get(id=menuitem_id)
	ingredients = menuitem.topping_set.order_by('name')
	context = {'menuitem': menuitem, 'ingredients': ingredients}
	return render(request, 'pizzas/toppings.html', context)
