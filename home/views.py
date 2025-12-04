from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def sobre(request):
    return HttpResponse("Sobre o Sistema Django.")

def contato(request):
    return HttpResponse("Página de Contato.")

def ajuda(request):
    return HttpResponse("Página de Ajuda.")