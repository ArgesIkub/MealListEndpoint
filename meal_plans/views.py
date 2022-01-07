from django.shortcuts import render

from meal_plans.models import Meals

# Create your views here.
def all_meals(request):
    all_meals = Meals.objects.all()
    return render(request, 'meal_plans/meals.html', {'meals': all_meals})

def create_meal(request):
    new_meal = Meals(name=request.POST['meal_name'])
    new_meal.save()
    all_meals = Meals.objects.all()
    return render(request, 'meal_plans/meals.html', {'meals': all_meals})

