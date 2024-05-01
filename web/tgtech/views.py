from django.shortcuts import render
from django.http import HttpResponse
from app import send_message


# def form(request):
#     if request.method == 'POST':
#         send_message(f'{request.POST}', f'{request.POST}', f'{request.POST}')

def index(request):
    if request.method == 'POST':
        send_message(f'{request.POST}', f'{request.POST}', f'{request.POST}')
    else:
        return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def oferta(request):
    return render(request, "oferta.html")

def cases(request):
    return render(request, "cases.html")

def happypc(request):
    return render(request, "happypc.html")

def posylochka(request):
    return render(request, "posylochka.html")