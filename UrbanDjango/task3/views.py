from django.shortcuts import render

# Create your views here.

def plat(request):
    return render(request, 'third_task/platform.html')

def games(request):
    context = {
        "first": "Alomic Heart",
        "secont": "Cyberpunk 2077",
        "third": "PayDay 2"
    }
    return render(request, 'third_task/games.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')
