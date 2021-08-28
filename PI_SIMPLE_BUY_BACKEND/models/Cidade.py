from models import BaseModel as model
import peewee as pw
from models.Estado import Estado


class Cidade(model.BaseModel):

        nome = pw.CharField()
        estado = pw.ForeignKeyField(Estado)