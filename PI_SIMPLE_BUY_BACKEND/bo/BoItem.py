
from models.Item import Item
from dao.GenericDao import GenericDao





class BoItem():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: Item):
                return self.dao.create(model)

        def update(self, model: Item):
                return self.dao.update(model)

        def delete(self, model: Item):
                return self.dao.delete(model)

        def selectAll(self, model: Item):
                return self.dao.selectAll(model)
