from converte.model import entrada
from django.shortcuts import render
from converte.model import logica
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
@requires_csrf_token
def retornaHtml(request):
    return render(request, "index.html")
def ctv(request):
    if request.method=='POST':
        tex=request.POST.get('texto')
        tex=novaView(tex)
    return render(request, "converterV.html")

def novaView(tex):
    falar=logica.Meio()
    falar.transformaTV(tex)
    #return render(request, "converterV.html")


def cvt(request):
    if request.method=='POST':
        texto=ouve(request)
    return render(request, "converterVT.html",{'texto':texto})

def ouve(request):
    texto=""
    dic={}
    escuta=entrada.Entrada()
    texto=escuta.ouvir()
    convertida=str(texto)
    #print(type(texto))
    #dic={'texto':convertida}
    #print(convertida)
    #return render(request, "converterVT.html",{'texto':convertida})
    return convertida
#ouve(request)
