from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Página Principal.")

def sobre(request):
    return HttpResponse("Sobre o Sistema Django.")