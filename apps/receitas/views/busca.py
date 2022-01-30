from django.shortcuts import render
from receitas.models import Receita

def buscar(request):
    """ Faz a busca de receitas no sistema """
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)
    