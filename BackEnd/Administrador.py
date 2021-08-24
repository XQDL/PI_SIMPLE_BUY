class Administrador:
    def __init__(self, id, nomeUsuario, senha, nome, email, telefone, empresa):
        self.id = id
        self.nomeUsuario = nomeUsuario
        self.senha = senha
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.empresa = empresa

    def cadastrarItem(self):
        print('Cadastar Item')

    def cadastrarComprador(self):
        print('Cadastrar Comprador')