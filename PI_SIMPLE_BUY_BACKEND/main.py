from models.CreateTable import CreateTable

from models.Administrador import Administrador
from models.Cidade import Cidade
from models.Classe import Classe
from models.ClasseFornecedor import ClasseFornecedor
from models.Comprador import Comprador
from models.Empresa import Empresa
from models.EmpresaCompradora import EmpresaCompradora
from models.Endereco import Endereco
from models.Estado import Estado
from models.Fornecedor import Fornecedor
from models.Frete import Frete
from models.Item import Item
from models.ItemNf import ItemNf
from models.ItemOf import ItemOf
from models.NotaFiscal import NotaFiscal
from models.OfNf import OfNf
from models.OrdemFornecimento import OrdemFornecimento

from bo.BoAdministrador import BoAdministrador
from bo.BoCidade import BoCidade
from bo.BoClasse import BoClasse
from bo.BoClasseFornecedor import BoClasseFornecedor
from bo.BoComprador import BoComprador
from bo.BoEmpresaCompradora import BoEmpresaCompradora
from bo.BoEndereco import BoEndereco
from bo.BoEstado import BoEstado
from bo.BoFornecedor import BoFornecedor
from bo.BoItem import BoItem
from bo.BoItemNf import BoItemNf
from bo.BoItemOf import BoItemOf
from bo.BoNotaFiscal import BoNotaFiscal
from bo.BoOfNf import BoOfNf
from bo.BoOrdemFornecimento import BoOrdemFornecimento




from bo.BoEstado import BoEstado

if __name__ == '__main__':

    # Criando tabelas
    create = CreateTable()
    create.createAll()

    # criando um estado
    estado = Estado(nome='Parana')
    boEstado = BoEstado()
    boEstado.create(estado)

    print(estado)

    # Selecionando todos os estados
    estados = boEstado.selectAll(Estado)

    print('Estados:')
    print(estados)

    # criando um cidade
    cidade = Cidade(nome='Lapas', estado=estado)
    boCidade = BoCidade()
    boCidade.create(cidade)

    # Alterando o nome do cidade
    cidade.nome = 'Lapa'

    boCidade.update(cidade)

    print(cidade)

    cidades = boCidade.selectAll(Cidade)
    print('Cidades:')
    print(cidades)


    endereco = Endereco(numero=123, cep='83750000', complemento='Casa', rua='Rua joão da cunha', cidade=cidade)
    boEndereco = BoEndereco()
    boEndereco.create(endereco)



    # Selecionando todos os estados
    enderecos = boEndereco.selectAll(Endereco)

    print('Endereços:')
    print(enderecos)

    endereco2 = Endereco(numero=321, cep='8140000', complemento='Apartamento', rua='Rua general Carneiro', cidade=cidade)
    boEndereco = BoEndereco()
    boEndereco.create(endereco2)

    # Selecionando todos os estados
    enderecos = boEndereco.selectAll(Endereco)

    print('Endereços:')
    print(enderecos)

    administrador = Administrador(nomeUsuario='AndreVinni89', senha='1234', nome='Andre Vinicius Vieira', email='andrevinnicius89@gmail.com', telefone='(41) 99999-9999')
    boAdministrador = BoEmpresaCompradora()
    boAdministrador.create(administrador)



    # Selecionando todos os estados
    administradores = boAdministrador.selectAll(EmpresaCompradora)

    print('Empresas compradoras:')
    print(administradores)


    empresaCompradora = EmpresaCompradora(nome='XQDL CORPORATIONS', cnpj='12345678910', telefone='4002-8922', endereco=endereco, administrador=administrador)
    boEmpresaCompradora = BoEmpresaCompradora()
    boEmpresaCompradora.create(empresaCompradora)



    # Selecionando todos os estados
    empresaCompradoras = boEmpresaCompradora.selectAll(EmpresaCompradora)

    print('Empresas compradoras:')
    print(empresaCompradoras)

    # criando um Comprador
    comprador = Comprador(nome='Adailson Almeida', nomeUsuario='ADA123', senha='123', email='adailson@xqdl.com.br', telefone='(41) 3547-8282', empresa=empresaCompradora )
    boComprador = BoComprador()
    boComprador.create(comprador)



    # Selecionando todos os Compradores
    compradores = boComprador.selectAll(Comprador)

    print('Compradores:')
    print(compradores)


    item = Item(descricao='Caderno 20 materiais', unidadeMedida='Un')
    boItem = BoItem()
    boItem.create(item)



    # Selecionando todos os estados
    itens = boItem.selectAll(Item)

    print("Itens:")
    print(itens)


    # criando um estado
    classe = Classe(nome='Materias administrativos')
    boClasse = BoClasse()
    boClasse.create(classe)



    # Selecionando todos os estados
    classes = boClasse.selectAll(Classe)

    print("Classes:")
    print(classes)

    # criando um estado
    fornecedor = Fornecedor(nome='Casas Bahia', cnpj='12345678910', telefone='4002-8787', endereco=endereco2)
    boFornecedor = BoFornecedor()
    boFornecedor.create(fornecedor)



    # Selecionando todos os estados
    fornecedores = boFornecedor.selectAll(Fornecedor)

    print("Fornecedores:")
    print(fornecedores)


    # criando um estado
    classeFornecedor = ClasseFornecedor(classeId=classe, fornecedorId=fornecedor)
    BoClasseFornecedor = BoClasseFornecedor()
    BoClasseFornecedor.create(classeFornecedor)

    # criando um estado
    ordemFornecimento = OrdemFornecimento(icms=3.0, ipi=2.0, frete='FOB', fornecedor=fornecedor, contratante=empresaCompradora, dataEntrega='18/09/2021', comprador=comprador )
    BordemFornecimento = BoOrdemFornecimento()
    BordemFornecimento.create(ordemFornecimento)

    # Selecionando todos os estados
    ordens_de_fornecimentos = BordemFornecimento.selectAll(OrdemFornecimento)


    print("Ordens de Fornecimento:")
    print(ordens_de_fornecimentos)


    # criando um estado
    itemOf = ItemOf(ItemId=item, OfId= ordemFornecimento, quantidade=12, valorUnitario=19.90, recebido=0, saldo=12)
    BoItemOf = BoItemOf()
    BoItemOf.create(itemOf)
