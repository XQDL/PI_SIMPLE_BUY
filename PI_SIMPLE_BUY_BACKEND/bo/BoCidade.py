
from models.Cidade import Cidade
from dao.GenericDao import GenericDao



class BoCidade():

        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: Cidade):
                return self.dao.create(model)

        def update(self, model: Cidade):
                return self.dao.update(model)

        def delete(self, model: Cidade):
                return self.dao.delete(model)

        def selectAll(self, model: Cidade):
                return self.dao.selectAll(model)