
import peewee as pw
from models.Endereco import Endereco
from models.Administrador import Administrador
from models import BaseModel as model


class EmpresaCompradora(model.BaseModel):
        nome = pw.CharField()
        cnpj = pw.CharField()
        endereco = pw.ForeignKeyField(Endereco)
        telefone = pw.CharField()
        administrador = pw.ForeignKeyField(Administrador)