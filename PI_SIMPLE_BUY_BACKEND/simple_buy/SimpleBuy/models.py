from django.db import models
from enum import Enum
from .enum.SituacaoOf import SituacaoOf

# Create your models here.



class Administrador(models.Model):
    nomeUsuario = models.CharField(unique=True, max_length=200)
    senha = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=500)
    telefone = models.CharField(max_length=200)
    plano = models.IntegerField()

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
    complemento = models.CharField(max_length=200, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.rua + ', ' +self.numero + ', ' + self.cidade

class Classe(models.Model):
    nome = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.nome



class Fornecedor(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    cnpj = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=500, null=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=200)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome





class EmpresaCompradora(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    cnpj = models.CharField(max_length=200, unique=True)
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
    descricao = models.CharField(unique=True, max_length=200)
    unidadeMedida = models.CharField(max_length=200)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao


class OrdemFornecimento(models.Model):
        fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
        contratante = models.ForeignKey(EmpresaCompradora, on_delete=models.CASCADE)
        comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
        situacao = models.CharField(max_length=200, default=SituacaoOf.COMPRADOR_NEGOCIANDO.value)
        valor_total = models.FloatField(default=0)

class NotaFiscal(models.Model):
    numeroNota = models.IntegerField()
    empresaEmitente = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    empresaDestinada = models.ForeignKey(EmpresaCompradora, on_delete=models.CASCADE)
    ofs = models.ManyToManyField(OrdemFornecimento)

    def __str__(self):
        return self.numeroNota



class Itens_of(models.Model):
    cod_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    num_of = models.ForeignKey(OrdemFornecimento, on_delete=models.CASCADE)
    valor_unitario = models.FloatField(default=0)
    valor = models.FloatField()
    quantidade = models.FloatField()
    recebido = models.FloatField(default=0)
    ipi = models.FloatField()
    icms = models.FloatField()
    dataEntrega = models.DateTimeField(null=True)
    frete = models.CharField(max_length=200, null=True)

class Itens_nf(models.Model):
    cod_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    num_of = models.ForeignKey(OrdemFornecimento, null=True, on_delete=models.CASCADE)
    num_nf = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    valor_unitario = models.FloatField(default=0)
    valor = models.FloatField()
    quantidade = models.FloatField()
    ipi = models.FloatField()
    icms = models.FloatField()
    frete = models.CharField(max_length=200, null=True)


class Item_pendente_cotacao(models.Model):
    cod_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    data = models.DateTimeField()
    solicitante_adm = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True)
    solicitante_comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.cod_item.descricao


class UnidadeMedida(Enum):
    KG = 1
    UN = 2
    PA = 3
    MT = 4
    LT = 5
