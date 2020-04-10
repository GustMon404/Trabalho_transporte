from django.db import models


class Cargo(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=10)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    descricao = models.CharField(max_length=150)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)

    def __str__(self):
        return self.descricao

class Solicitacao(models.Model):
    origem = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    data_hora = models.DateTimeField()
    solicitante = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.origem

class Atendimento(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
    motorista = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)