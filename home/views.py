from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import ContatoForm, ProdutoForm 

# --- FUNÇÕES AUXILIARES E LISTA DE PRODUTOS ---

# Função para fornecer a lista de produtos COMPLETA (agora com Estoque)
def get_produto_lista():
    
    return [
        {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00', 'estoque': 10},
        {'id': 2, 'nome': 'Monitor', 'preco': '500,00', 'estoque': 10},
        {'id': 3, 'nome': 'Teclado', 'preco': '80,00', 'estoque': 10},
        {'id': 4, 'nome': 'Mouse', 'preco': '40,00', 'estoque': 10},
        {'id': 5, 'nome': 'Impressora', 'preco': '600,00', 'estoque': 10},
        {'id': 6, 'nome': 'Scanner', 'preco': '700,00', 'estoque': 10},
        {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00', 'estoque': 10},
        {'id': 8, 'nome': 'Headset', 'preco': '120,00', 'estoque': 10},
        {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00', 'estoque': 10},
        {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00', 'estoque': 10},
        {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00', 'estoque': 10},
        {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00', 'estoque': 10},
        {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00', 'estoque': 10},
    ]




def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    # Lógica de POST e GET aqui (deve ser aprimorada, por enquanto só GET)
    form = ContatoForm()
    context = {
        'form': form    
        }
    return render(request, "contato.html", context)

def ajuda(request):
    return render(request, "ajuda.html")

def exibir_item(request, id ):
    return render(request, "exibir_item.html", {'id': id})

def perfil(request, usuario):
    nome_exibicao = usuario.replace('%20', ' ')
    contexto = {
        'usuario': nome_exibicao
    }
    return render(request, "perfil.html", contexto)

def dia_da_semana(request, dia):
    dias_mapa = {
        1: "Domingo", 2: "Segunda-feira", 3: "Terça-feira", 4: "Quarta-feira",
        5: "Quinta-feira", 6: "Sexta-feira", 7: "Sábado",
    }
    
    if 1 <= dia <= 7:
        nome_dia = dias_mapa[dia]
    else:
        nome_dia = "Dia inválido"
    
    contexto = {
        'numero_dia': dia,
        'nome_dia': nome_dia,
    }
    return render(request, "diasemana.html", contexto)


# --- VIEWS DE PRODUTO (Lista e CRUD) ---

def produto(request):
    contexto = {
        'lista': get_produto_lista(),
    }
    return render(request, 'produto/lista.html',contexto)


def form_produto(request):
    # Lógica de POST e GET para Novo Produto (Se estiver no modo "Novo")
    if request.method == 'POST':
        form = ProdutoForm(request.POST) 
        if form.is_valid():
           
            return redirect('produto') 
    else:
        form = ProdutoForm()    
   
    contexto = {
        'form': form
    }   
    
    # Se for GET (novo) ou POST inválido
    return render(request, 'produto/formulario.html', contexto)


def detalhes_produto(request, id):
    lista = get_produto_lista()
    produto_detalhes = next((item for item in lista if item['id'] == id), None)
    
    contexto = {
        'id': id,
        'produto': produto_detalhes
    }
    return render(request, 'produto/detalhes.html', contexto)



def editar_produto(request, id):
    lista = get_produto_lista()
    produto_existente = next((item for item in lista if item['id'] == id), None)

    if produto_existente is None:
        return redirect('produto') 

    if request.method == 'POST':
        form = ProdutoForm(request.POST) 
        
        if form.is_valid():
            
            produto_existente['nome'] = form.cleaned_data['nome']
            produto_existente['preco'] = form.cleaned_data['preco']
            produto_existente['estoque'] = form.cleaned_data['estoque'] 
            
            print(f"Produto ID {id} ALTERADO com sucesso!")
            return redirect('produto') 
            
    else:
        # Lógica GET: Pré-preenche o formulário
        # CORRIGIDO: Inclui o valor do estoque para pré-preenchimento
        form = ProdutoForm(initial={
            'nome': produto_existente['nome'],
            'preco': produto_existente['preco'],
            'estoque': produto_existente['estoque'], 
        })
    
    contexto = {
        'id': id,
        'form': form,
        'titulo': f"Editar Produto ID {id} - {produto_existente['nome']}",
    }
    return render(request, 'produto/formulario.html', contexto)



from django.shortcuts import render, redirect 

def excluir_produto(request, id):
    
    lista = get_produto_lista() 
    
    produto_existente = next((item for item in lista if item['id'] == id), None)

    if request.method == 'POST':
        # Lógica POST: Confirmação de Exclusão
        
        if produto_existente is not None:
            # A mensagem de sucesso DEVE ser exibida no terminal do servidor
            print(f"Produto ID {id} ('{produto_existente['nome']}') EXCLUÍDO com sucesso! (Simulação)")
            
        
        else:
             print(f"AVISO: Tentativa de exclusão do Produto ID {id}, mas o produto não foi encontrado na lista.")
             
        return redirect('produto')
            
    else:
        # Lógica GET: Exibir a tela de confirmação
        contexto = {
            'id': id,
            'produto': produto_existente # Passa o produto para o template, se necessário
        }
        return render(request, 'produto/excluir.html', contexto)
