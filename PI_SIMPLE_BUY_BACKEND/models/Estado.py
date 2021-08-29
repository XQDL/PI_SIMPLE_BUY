
from models import BaseModel as model
import peewee as pw



class Estado(model.BaseModel):
    nome = pw.CharField()

    def __str__(self):
        return self.nome

