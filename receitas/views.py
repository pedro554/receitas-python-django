# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'receitas/pages/home.html',
                  context={"nome": "Pedro"})


def receitas(request, id):
    return render(request, 'receitas/pages/receita-view.html',
                  context={"nome": "Pedro"})
