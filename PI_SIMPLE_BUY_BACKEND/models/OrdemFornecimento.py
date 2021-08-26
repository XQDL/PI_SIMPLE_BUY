import Empresa
from models import BaseModel as model
import peewee as pw
import EmpresaCompradora, Fornecedor, Item, Comprador


class OrdemFornecimento(model.BaseModel):

        itens = pw.ForeignKeyField(Item)
        valorUnitario = pw.FloatField()
        icms = pw.FloatField()
        ipi = pw.FloatField()
        frete = pw.CharField()
        fornecedor = pw.ForeignKeyField(Fornecedor)
        contratante = pw.ForeignKeyField(EmpresaCompradora)
        dataEntrega = pw.DateTimeField()
        comprador = pw.ForeignKeyField(Comprador)