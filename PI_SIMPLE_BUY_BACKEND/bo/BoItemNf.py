from models.ItemNf import ItemNf
from dao.GenericDao import GenericDao


class BoItemNf():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: ItemNf):
                return self.dao.create(model)

        def update(self, model: ItemNf):
                return self.dao.update(model)

        def delete(self, model: ItemNf):
                return self.dao.delete(model)

        def selectAll(self, model: ItemNf):
                return self.dao.selectAll(model)
