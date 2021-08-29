from models.CreateTable import CreateTable
from models.Estado import Estado
from dao.GenericDao import GenericDao

if __name__ == '__main__':

    # Criando tabelas
    create = CreateTable()
    create.createAll()

    # criando um estado
    estado = Estado(nome='Parana')
    dao = GenericDao()
    dao.create(estado)

    # Alterando o nome do estado
    estado.nome = 'Santa Catarina'

    dao.update(estado)
    print(estado)

    # Selecionando todos os estados
    estados = dao.selectAll(Estado)

    print(estados)

    # Deletando um estado especifico
    dao.delete(estado)

    estados = dao.selectAll(Estado)

    print(estados)



