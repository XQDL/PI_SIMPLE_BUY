from models.Administrador import Administrador
import peewee


if __name__ == '__main__':
    try:
        Administrador.create_table()
        print("Tabela 'Author' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Author' ja existe!")

    # adm = Administrador.create(
    #     nomeUsuario = 'AndreVinni89',
    #     senha = '123',
    #     nome = 'Andre',
    #     email = 'Andrevinnicius89@gmail.com',
    #     telefone = "41997175818"
    # )

    res = Administrador.select()
    for r in res:
        print(r.nomeUsuario)