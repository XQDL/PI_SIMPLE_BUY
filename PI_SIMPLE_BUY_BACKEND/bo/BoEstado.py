
from models.Estado import Estado
from dao.GenericDao import GenericDao



class BoEstado():
    def __init__(self):
        self.dao = GenericDao()

    def create(self, model: Estado):
        return self.dao.create(model)

    def update(self, model: Estado):
        return self.dao.update(model)

    def delete(self, model: Estado):
        return self.dao.delete(model)

    def selectAll(self, model: Estado):
        return self.dao.selectAll(model)
