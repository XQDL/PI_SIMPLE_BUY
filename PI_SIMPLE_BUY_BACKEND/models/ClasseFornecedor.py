from models import BaseModel as model
import peewee as pw
from models.Classe import Classe
from models.Fornecedor import Fornecedor


class ClasseFornecedor(model.BaseModel):
    classeId = pw.ForeignKeyField(Classe)
    fornecedorId = pw.ForeignKeyField(Fornecedor)
