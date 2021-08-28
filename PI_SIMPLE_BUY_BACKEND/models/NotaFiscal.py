
from models import BaseModel as model
import peewee as pw
from models.EmpresaCompradora import EmpresaCompradora
from models.Fornecedor import Fornecedor
from models.Item import Item


class NotaFiscal(model.BaseModel):
        numeroNota = pw.IntegerField(unique=True)
        empresaEmitente = pw.ForeignKeyField(Fornecedor)
        empresaDestinada = pw.ForeignKeyField(EmpresaCompradora)
        icms = pw.FloatField()
        ipi = pw.FloatField()