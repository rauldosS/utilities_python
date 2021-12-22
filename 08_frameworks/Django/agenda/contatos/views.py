from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato, Categoria

from django.db.models import Q, Value
from django.db.models.functions import Concat

from django.contrib import messages

# Create your views here.
def home(request):
    # messages.add_message(request, messages.ERROR, 'Ocorreu um erro!')

    contatos = Contato.objects.all().order_by('nome').filter(exibir=True)
    paginator = Paginator(contatos, 5)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/home.html', {'contatos': contatos})

def contato(request, pk):
    contato = get_object_or_404(Contato, id=pk)

    if not contato.exibir:
        raise Http404

    return render(request, 'contatos/contato.html', {'contato': contato})
    
    """ Tratando error 404
    try:
        pass
    except Contato.DoesNotExist as e:
        raise Http404
    """

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo termo não pode ficar vazio.')
        return redirect('home')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    ).order_by('nome')

    paginator = Paginator(contatos, 5)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/home.html', {'contatos': contatos})