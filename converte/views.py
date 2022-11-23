from django.shortcuts import render
from converte.model import logica
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
@requires_csrf_token
def retornaHtml(request):
    return render(request, "index.html")
def ctv(request):
    """falar=logica.Meio()
    falar.transformaTV(texto)"""
    return render(request, "converterV.html")
def cvt(request):
    return render(request, "converterVT.html")
