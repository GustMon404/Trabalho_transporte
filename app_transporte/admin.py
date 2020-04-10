from django.contrib import admin
from .models import *
@admin.register(Cargo, Departamento, Funcionario, Solicitacao, Veiculo, Atendimento)
class TransporteAdmin(admin.ModelAdmin):
    pass
# Register your models here.