from django.urls import path
from app_transporte.views import *

urlpatterns = [
    path('solicitacao/', Tabela, name = 'solicitacao_tabela'),
    path('solicitacao/<int:funcionario_id>', Tabela_id, name = 'solicitacao_tabela_id'),
    path('solicitacao/informacoes/<int:solicitacao_id>', Tabela_Informacoes_Solicitacao, name = 'informacoes_solicitante'),
    path('veiculo', Tabela_Veiculo, name = 'veiculo_tabela'),
    path('veiculo/informacoes/<int:veiculo_id>', Tabela_Informacoes_Veiculo, name = 'informacoes_veiculo'),
    path('funcionario', Tabela_Funcionario, name = 'funcionario_tabela'),
    path('funcionario/informacoes/<int:funcionario_id>', Tabela_Informacoes_Funcionario, name = 'informacoes_funcionario'),
]