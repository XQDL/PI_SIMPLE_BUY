from models.Empresa import Empresa
import peewee as pw

from models.Administrador import Administrador



class EmpresaCompradora(Empresa):
        administrador = pw.ForeignKeyField(Administrador)