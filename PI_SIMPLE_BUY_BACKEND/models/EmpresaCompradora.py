import Empresa
from models import BaseModel as model
import peewee as pw
import Comprador, Administrador


class EmpresaCompradora(Empresa.Empresa):

        compradores = pw.ForeignKeyField(Comprador)
        administrador = pw.ForeignKeyField(Administrador)