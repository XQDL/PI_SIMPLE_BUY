from models.Endereco import Endereco
from dao.GenericDao import GenericDao


class BoEndereco():
    def __init__(self):
        self.dao = GenericDao()

    def create(self, model: Endereco):
        return self.dao.create(model)

    def update(self, model: Endereco):
        return self.dao.update(model)

    def delete(self, model: Endereco):
        return self.dao.delete(model)

    def selectAll(self, model: Endereco):
        return self.dao.selectAll(model)
