from models.Administrador import Administrador
from models.Cidade import Cidade
from models.Classe import Classe
from models.Comprador import Comprador
from models.EmpresaCompradora import EmpresaCompradora
from models.Endereco import Endereco
from models.Estado import Estado
from models.Fornecedor import Fornecedor
from models.Item import Item
from models.NotaFiscal import NotaFiscal
from models.OrdemFornecimento import OrdemFornecimento
from models.OfNf import OfNf
from models.ItemNf import ItemNf
from models.ItemOf import ItemOf
from models.ClasseFornecedor import ClasseFornecedor


import peewee


class CreateTable:


    def createAll(self):
        try:
            EmpresaCompradora.create_table()
            print("Tabela 'EmpresaCompradora' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'EmpresaCompradora' ja existe!")


        try:
            Administrador.create_table()
            print("Tabela 'Administrador' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Administrador' ja existe!")

        try:
            Cidade.create_table()
            print("Tabela 'Cidade' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Cidade' ja existe!")

        try:
            Classe.create_table()
            print("Tabela 'Classe' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Classe' ja existe!")

        try:
            Comprador.create_table()
            print("Tabela 'Comprador' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Comprador' ja existe!")


        try:
            Endereco.create_table()
            print("Tabela 'Endereco' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Endereco' ja existe!")

        try:
            Estado.create_table()
            print("Tabela 'Estado' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Estado' ja existe!")

        try:
            Fornecedor.create_table()
            print("Tabela 'Fornecedor' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Fornecedor' ja existe!")

        try:
            Item.create_table()
            print("Tabela 'Item' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Item' ja existe!")

        try:
            NotaFiscal.create_table()
            print("Tabela 'NotaFiscal' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'NotaFiscal' ja existe!")

        try:
            OrdemFornecimento.create_table()
            print("Tabela 'OrdemFornecimento' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'OrdemFornecimento' ja existe!")

        try:
            OfNf.create_table()
            print("Tabela 'OfNf' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'OfNf' ja existe!")

        try:
            ItemOf.create_table()
            print("Tabela 'ItemOf' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'ItemOf' ja existe!")

        try:
            ItemNf.create_table()
            print("Tabela 'ItemNf' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'ItemNf' ja existe!")

        try:
            ClasseFornecedor.create_table()
            print("Tabela 'ClasseFornecedor' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'ClasseFornecedor' ja existe!")

