from django.shortcuts import render
from django.http import Http404
from .models import *


def Tabela(request):
    solicitacao = Solicitacao.objects.all()
    return render(request, 'app_transporte/Tabela_solicitacao.html', {'solicitacao': solicitacao})


def Tabela_id(request, funcionario_id):
    solicitacao = Solicitacao.objects.filter(solicitante=funcionario_id)
    return render(request, 'app_transporte/Tabela_solicitacao.html', {'solicitacao': solicitacao})


def Tabela_Informacoes_Solicitacao(request, solicitacao_id):
    solicitacao = Solicitacao.objects.get(pk=solicitacao_id)
    return render(request, 'app_transporte/Informacoes_solicitante.html', {'solicitacao': solicitacao})

def Tabela_Veiculo(request):
    veiculo = Veiculo.objects.all()
    return render(request, 'app_transporte/Tabela_veiculo.html',{'veiculo' : veiculo})

def Tabela_Informacoes_Veiculo(request, veiculo_id):
    veiculo = Veiculo.objects.get(pk=veiculo_id)
    return render(request, 'app_transporte/Informacoes_veiculo.html', {'veiculo' : veiculo})

def Tabela_Funcionario(request):
    funcionario = Funcionario.objects.all()
    return render(request, 'app_transporte/Tabela_funcionario.html',{'funcionario' : funcionario})

def Tabela_Informacoes_Funcionario(request, funcionario_id):
    funcionario = Funcionario.objects.get(pk=funcionario_id)
    return render(request, 'app_transporte/Informacoes_funcionario.html', {'funcionario' : funcionario})

# Create your views here.
