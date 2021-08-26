import Empresa
from models import BaseModel as model
import peewee as pw
import Comprador, Administrador


class Item(model.BaseModel):
        descricao = pw.CharField()
        unidadeMedida = pw.CharField()