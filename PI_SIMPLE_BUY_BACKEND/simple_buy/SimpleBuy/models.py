from django.db import models
from enum import Enum

# Create your models here.



class Administrador(models.Model):
    nomeUsuario = models.CharField(unique=True, max_length=200)
    senha = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=500)
    telefone = models.CharField(max_length=200)
    plano = models.IntegerField();

    def __str__(self):
        return self.nomeUsuario

class Estado(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    cep = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.rua + ', ' +self.numero + ', ' + self.cidade

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Classe(models.Model):
    nome = models.CharField(unique=True, max_length=200)
    fornecedores = models.ManyToManyField(Fornecedor)

    def __str__(self):
        return self.nome




class EmpresaCompradora(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=200)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome


class Comprador(models.Model):
    nomeUsuario = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    empresa = models.ForeignKey(EmpresaCompradora, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomeUsuario







class Frete(Enum):
    CIF = 1
    FOB = 2

class Item(models.Model):
    descricao = models.CharField(max_length=200)
    unidadeMedida = models.CharField(max_length=200)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao


class OrdemFornecimento(models.Model):
        frete = models.CharField(max_length=200)
        fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
        contratante = models.ForeignKey(EmpresaCompradora, on_delete=models.CASCADE)
        dataEntrega = models.DateTimeField()
        comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)


class NotaFiscal(models.Model):
    numeroNota = models.IntegerField(unique=True)
    empresaEmitente = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    empresaDestinada = models.ForeignKey(EmpresaCompradora, on_delete=models.CASCADE)
    ofs = models.ManyToManyField(OrdemFornecimento)

    def __str__(self):
        return self.numeroNota



class itens_of(models.Model):
    cod_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    num_of = models.ForeignKey(OrdemFornecimento, on_delete=models.CASCADE)
    valor = models.FloatField()
    quantidade = models.FloatField()
    ipi = models.FloatField()
    icms = models.FloatField()


class itens_nf(models.Model):
    cod_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    num_nf = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    valor = models.FloatField()
    quantidade = models.FloatField()
    ipi = models.FloatField()
    icms = models.FloatField()



class UnidadeMedida(Enum):
    KG = 1
    UN = 2
    PA = 3
    MT = 4
    LT = 5
