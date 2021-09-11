from models.CreateTable import CreateTable
from models.Estado import Estado
from bo.BoEstado import BoEstado

if __name__ == '__main__':

    # Criando tabelas
    create = CreateTable()
    create.createAll()

    # criando um estado
    estado = Estado(nome='Parana')
    boEstado = BoEstado()
    boEstado.create(estado)

    # Alterando o nome do estado
    estado.nome = 'Santa Catarina232'

    boEstado.update(estado)
    print(estado)

    # Selecionando todos os estados
    estados = boEstado.selectAll(Estado)

    print(estados)

    # Deletando um estado especifico
    # boEstado.delete(estado)

    estados = boEstado.selectAll(Estado)

    print(estados)



