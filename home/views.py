from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from datetime import datetime

def index(request):
    response = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        try:
            usuario = Usuario(cpf=cpf, nome=nome, data_nascimento=data_nascimento)
            usuario.save()
            response = 'Usuário cadastrado com sucesso!'
        except Exception as e:
            response = f'Erro ao cadastrar usuário: {e}'
    elif request.method == 'GET' and 'nome' in request.GET:  # Verifica se 'nome' está realmente na solicitação GET
        nome = request.GET.get('nome')
        if nome:  # Apenas faça a consulta se 'nome' não for vazio
            try:
                usuario = Usuario.objects.get(nome=nome)
                data_nascimento_formatada = usuario.data_nascimento.strftime('%d/%m/%Y')
                response = f'Nome: {usuario.nome}<br>CPF: {usuario.cpf}<br>Data de Nascimento: {data_nascimento_formatada}'
            except Usuario.DoesNotExist:
                response = 'Usuário não encontrado.'

    return render(request, 'index.html', {'response': response})
