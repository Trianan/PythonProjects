from django.shortcuts import render

def index(request):
	"""Home page for Meal Planner"""
	return render(request, 'meal_plans/index.html')
