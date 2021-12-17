from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def game(request):
    return render(request, 'main/game.html')

def D2B(request):
    return render(request, 'main/D2B.html')

def D2H(request):
    return render(request, 'main/D2H.html')

def B2D(request):
    return render(request, 'main/B2D.html')

def B2H(request):
    return render(request, 'main/B2H.html')

def H2D(request):
    return render(request, 'main/H2D.html')

def H2B(request):
    return render(request, 'main/H2B.html')