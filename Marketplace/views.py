from django.shortcuts import render

def barra_principal(request):
    return render(request, 'Barra_marketplace.html')