from models import BaseModel as model
import peewee as pw


class Administrador(model.BaseModel):

    nomeUsuario = pw.CharField(unique=True)
    senha = pw.CharField()
    nome = pw.CharField()
    email = pw.CharField()
    telefone = pw.CharField()



    def cadastrarItem(self):
        print('Cadastar Item')

    def cadastrarComprador(self):
        print('Cadastrar Comprador')