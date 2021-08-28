from models import BaseModel as model
import peewee as pw
from models.EmpresaCompradora import EmpresaCompradora

class Comprador(model.BaseModel):

    nomeUsuario = pw.CharField()
    senha = pw.CharField()
    nome = pw.CharField()
    email = pw.CharField()
    telefone = pw.CharField()
    empresa = pw.ForeignKeyField(EmpresaCompradora)

    def cadastrarItem(self):
        print('Cadastar Item')

    def gerarOrdemFornecimento(self):
        print('Gerar Ordem de Fornecimento')