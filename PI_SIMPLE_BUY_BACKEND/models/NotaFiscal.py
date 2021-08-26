import Empresa
from models import BaseModel as model
import peewee as pw
import EmpresaCompradora, Fornecedor, Item



class NotaFiscal:
        numeroNota = pw.IntegerField(unique=True)
        empresaEmitente = pw.ForeignKeyField(Fornecedor)
        empresaDestinada = pw.ForeignKeyField(EmpresaCompradora)
        itens = pw.ForeignKeyField(Item)