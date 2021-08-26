from models import BaseModel as model
import peewee as pw



class Empresa(model.BaseModel):
        nome = pw.CharField()
        cnpj = pw.CharField()
        endereco = pw.CharField()
        telefone = pw.CharField()