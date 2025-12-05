from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")

def ajuda(request):
    return render(request, "ajuda.html")

def perfil(request, usuario):
    # Decodifica a string da URL: substitui '%20' por espaço
    nome_exibicao = usuario.replace('%20', ' ')
    
    # Passa o nome decodificado para o template no contexto
    contexto = {
        'usuario': nome_exibicao # Agora envia 'Daniel Maia'
    }
    return render(request, "perfil.html", contexto)

def dia_da_semana(request, numero):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }
    
    if 1 <= numero <= 7:
        nome_dia = dias[numero]
    else:
        nome_dia = "Dia inválido"
    
    contexto = {
        'numero_dia': numero,
        'nome_dia': nome_dia,
    }
    return render(request, "diasemana.html", contexto)