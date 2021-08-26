from models import BaseModel as model
import peewee as pw
import EmpresaCompradora


class Administrador(model.BaseModel):

    nomeUsuario = pw.CharField(unique=True)
    senha = pw.CharField()
    nome = pw.CharField()
    email = pw.CharField()
    telefone = pw.CharField()
    empresa = pw.ForeignKeyField(EmpresaCompradora)


    def cadastrarItem(self):
        print('Cadastar Item')

    def cadastrarComprador(self):
        print('Cadastrar Comprador')