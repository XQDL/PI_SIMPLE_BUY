
from models import BaseModel as model
import peewee as pw

from models.EmpresaCompradora import EmpresaCompradora
from models.Fornecedor import Fornecedor

from models.Comprador import Comprador


class OrdemFornecimento(model.BaseModel):


        icms = pw.FloatField()
        ipi = pw.FloatField()
        frete = pw.CharField()
        fornecedor = pw.ForeignKeyField(Fornecedor)
        contratante = pw.ForeignKeyField(EmpresaCompradora)
        dataEntrega = pw.DateTimeField()
        comprador = pw.ForeignKeyField(Comprador)