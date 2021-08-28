from models.Empresa import Empresa

import peewee as pw
from models.Classe import Classe

class Fornecedor(Empresa):

        classes = pw.ForeignKeyField(Classe)