from models.Fornecedor import Fornecedor
from dao.GenericDao import GenericDao


class Fornecedor():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: Fornecedor):
                return self.dao.create(model)

        def update(self, model: Fornecedor):
                return self.dao.update(model)

        def delete(self, model: Fornecedor):
                return self.dao.delete(model)

        def selectAll(self, model: Fornecedor):
                return self.dao.selectAll(model)
