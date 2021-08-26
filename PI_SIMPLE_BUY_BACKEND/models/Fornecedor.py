import Empresa
from models import BaseModel as model
import peewee as pw
import Classe

class Fornecedor(Empresa.Empresa):

        classes = pw.ForeignKeyField(Classe)