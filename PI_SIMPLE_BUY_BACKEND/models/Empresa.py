from models import BaseModel as model
import peewee as pw
from models.Endereco import Endereco


class Empresa(model.BaseModel):
        nome = pw.CharField()
        cnpj = pw.CharField()
        endereco = pw.ForeignKeyField(Endereco)
        telefone = pw.CharField()