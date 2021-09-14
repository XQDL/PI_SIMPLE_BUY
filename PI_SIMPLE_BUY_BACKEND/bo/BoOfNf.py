from models.OfNf import OfNf
from dao.GenericDao import GenericDao


class BoOfNf():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: OfNf):
                return self.dao.create(model)

        def update(self, model: OfNf):
                return self.dao.update(model)

        def delete(self, model: OfNf):
                return self.dao.delete(model)

        def selectAll(self, model: OfNf):
                return self.dao.selectAll(model)
