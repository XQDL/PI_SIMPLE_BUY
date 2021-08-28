from models import BaseModel as model
import peewee as pw


class Classe(model.BaseModel):

       nome = pw.CharField(unique=True)