import Empresa
from models import BaseModel as model
import peewee as pw
import Cidade, Administrador

class Endereco(model.BaseModel):
        rua = pw.CharField()
        numero = pw.IntegerField()
        cep = pw.CharField()
        complemento = pw.CharField()
        cidade = pw.ForeignKeyField(Cidade)