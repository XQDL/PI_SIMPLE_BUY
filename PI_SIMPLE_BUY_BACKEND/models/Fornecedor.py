from models import BaseModel as model
import peewee as pw
from models.Endereco import Endereco

from models.Classe import Classe

class Fornecedor(model.BaseModel):
    nome = pw.CharField()
    cnpj = pw.CharField()
    endereco = pw.ForeignKeyField(Endereco)
    telefone = pw.CharField()

