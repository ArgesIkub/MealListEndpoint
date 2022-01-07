
from django.urls.conf import path

from meal_plans.views import all_meals, create_meal

urlpatterns = [
    path('all_meals/', all_meals, name='all-meals'),
    path('create_meal', create_meal, name='create-meal')
]
