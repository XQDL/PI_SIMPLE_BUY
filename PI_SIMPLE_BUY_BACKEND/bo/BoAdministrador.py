
from models.Administrador import Administrador
from dao.GenericDao import GenericDao

class BoAdministrador():

    def __init__(self):
        self.dao = GenericDao()

    def create(self, model: Administrador):
        return self.dao.create(model)


    def update(self, model: Administrador):
        return self.dao.update(model)


    def delete(self, model: Administrador):
        return self.dao.delete(model)

    def selectAll(self, model: Administrador):
        return self.dao.selectAll(model)