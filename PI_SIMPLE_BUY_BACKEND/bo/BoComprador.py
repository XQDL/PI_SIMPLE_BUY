from models.Comprador import Comprador
from dao.GenericDao import GenericDao

class BoComprador():
    def __init__(self):
        self.dao = GenericDao()

    def create(self, model: Comprador):
        return self.dao.create(model)

    def update(self, model: Comprador):
        return self.dao.update(model)

    def delete(self, model: Comprador):
        return self.dao.delete(model)

    def selectAll(self, model: Comprador):
        return self.dao.selectAll(model)
