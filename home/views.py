from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")

def ajuda(request):
    return render(request, "ajuda.html")

def exibir_item(request, id ):
    return render(request, "exibir_item.html", {'id': id})

def perfil(request, usuario):
    # Decodifica a string da URL: substitui '%20' por espaço
    nome_exibicao = usuario.replace('%20', ' ')
    
    # Passa o nome decodificado para o template no contexto
    contexto = {
        'usuario': nome_exibicao # Agora envia 'Daniel Maia'
    }
    return render(request, "perfil.html", contexto)

def dia_da_semana(request, dia): # 💡 Usar 'dia' para corresponder ao urls.py
    # Usar um nome de variável diferente para o dicionário (ex: dias_mapa)
    dias_mapa = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }
    
    # A lógica de verificação agora compara apenas inteiros
    if 1 <= dia <= 7:
        nome_dia = dias_mapa[dia] # Acessando o dicionário com o INT 'dia'
    else:
        nome_dia = "Dia inválido"
    
    contexto = {
        'numero_dia': dia,
        'nome_dia': nome_dia,
    }
    # Assumindo que você tem um template chamado 'diasemana.html'
    return render(request, "diasemana.html", contexto)

# ... (suas outras views, como index, sobre, etc.)

# 💡 Adicione esta nova função 'produto'
def produto(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html',contexto)
