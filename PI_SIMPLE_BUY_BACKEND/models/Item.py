from models import BaseModel as model
import peewee as pw



class Item(model.BaseModel):
        descricao = pw.CharField()
        unidadeMedida = pw.CharField()
        valor = pw.FloatField()
        quantidade = pw.FloatField()