from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def game(request):
    return render(request, 'main/game.html')


def D2B(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])

        bilkeluar = str('123')
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        return render(request, 'main/D2B.html', context)

    else:
        return render(request, 'main/D2B.html', {})


def D2H(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])

        bilkeluar = str('123')
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        return render(request, 'main/D2B.html', context)

    else:
        return render(request, 'main/D2B.html', {})

def B2D(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])

        bilkeluar = str('123')
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        return render(request, 'main/D2B.html', context)

    else:
        return render(request, 'main/D2B.html', {})

def B2H(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])

        bilkeluar = str('123')
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        return render(request, 'main/D2B.html', context)

    else:
        return render(request, 'main/D2B.html', {})

def H2D(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])

        bilkeluar = str('123')
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        return render(request, 'main/D2B.html', context)

    else:
        return render(request, 'main/D2B.html', {})

def H2B(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])

        bilkeluar = str('123')
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        return render(request, 'main/D2B.html', context)

    else:
        return render(request, 'main/D2B.html', {})