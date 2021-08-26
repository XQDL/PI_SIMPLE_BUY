from models import BaseModel as model
import peewee as pw
import Estado


class Cidade(model.BaseModel):

        nome = pw.CharField()
        estado = pw.ForeignKeyField(Estado)