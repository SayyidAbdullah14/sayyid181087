from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def game(request):
    return render(request, 'main/game.html')


def D2B(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])
        bilkeluar = bin(bilmasuk).replace("0b", "")
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        print(context)
        return render(request, 'main/D2B.html', context)
    else:
        return render(request, 'main/D2B.html', {})

def D2H(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])
        bilkeluar= int(oct(bilmasuk) .replace("0o",""))
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        print(context)
        return render(request, 'main/D2H.html', context)
    else:
        return render(request, 'main/D2H.html', {})

def B2D(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])
        a = 10
        b = 1
        desimal = 0
        p = 0
        while b <= bilmasuk:
            c = bilmasuk % a
            d = c / b
            desimal = desimal + d*(2**p)
            a = a * 10
            b = b * 10
            p = p + 1
        bilkeluar = int(desimal)
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        print(context)
        return render(request, 'main/B2D.html', context)

    else:
        return render(request, 'main/B2D.html', {})

def B2H(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])
        bilkeluar = oct(bilmasuk).replace("0o", "")
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        print(context)
        return render(request, 'main/B2H.html', context)
    else:
        return render(request, 'main/B2H.html', {})

def H2D(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])
        bilkeluar = bin(bilmasuk).replace("0b", "")
        bilmasuk = int(bilkeluar)
        a = 10
        b = 1
        desimal = 0
        p = 0
        while b <= bilmasuk:
            c = bilmasuk % a
            d = c / b
            desimal = desimal + d * (2 ** p)
            a = a * 10
            b = b * 10
            p = p + 1
        bilkeluar = int(desimal)
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        print(context)
        return render(request, 'main/H2D.html', context)
    else:
        return render(request, 'main/H2D.html', {})

def H2B(request):
    if request.method == 'POST':
        bilmasuk = int(request.POST['masuk'])
        bilkeluar = bin(bilmasuk).replace("0b", "")
        context = {'masuk': bilmasuk,
                   'keluar': bilkeluar,
                   }
        print(context)
        return render(request, 'main/H2B.html', context)
    else:
        return render(request, 'main/H2B.html', {})