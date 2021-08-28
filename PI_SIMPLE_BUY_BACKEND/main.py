from models.CreateTable import CreateTable
from models.Estado import Estado
from dao.GenericDao import GenericDao

if __name__ == '__main__':
    create = CreateTable()
    create.createAll()

    estado = Estado(nome='Rio de Janeiro')
    dao = GenericDao()
    dao.create(estado)

    estado.nome = 'Paraiba'

    dao.update(estado)

    print(estado)

    estados = dao.selectAll(Estado)

    print(estados)

    for i in estados:
        print(i)

    dao.delete(estado)

    estados = dao.selectAll(Estado)

    for i in estados:
        print(i)



