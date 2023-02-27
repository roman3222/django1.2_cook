from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def get_hello(requests):
   return render(requests, 'index.html')

def get_dish(requests, dish_name):
    serving = int(requests.GET.get('servings', '1'))
    recipe = DATA.get(dish_name)
    if recipe:
        context = {
            'dish': f'{dish_name}:',
            'recipe': {ingredient: quantity * serving for ingredient, quantity in recipe.items()},
        }
        return render(requests, 'dishes.html', context)
    else:
        return HttpResponse('Recipe not found', status=404)


