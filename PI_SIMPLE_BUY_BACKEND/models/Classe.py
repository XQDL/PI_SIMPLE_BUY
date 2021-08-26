from models import BaseModel as model
import peewee as pw
import EmpresaCompradora

class Classe(model.BaseModel):

       nome = pw.CharField(unique=True)