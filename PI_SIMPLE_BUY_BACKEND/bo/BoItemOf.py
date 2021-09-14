from models.ItemOf import ItemOf
from dao.GenericDao import GenericDao


class BoItemOf():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: ItemOf):
                return self.dao.create(model)

        def update(self, model: ItemOf):
                return self.dao.update(model)

        def delete(self, model: ItemOf):
                return self.dao.delete(model)

        def selectAll(self, model: ItemOf):
                return self.dao.selectAll(model)
