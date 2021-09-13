from models.Classe import Classe
from dao.GenericDao import GenericDao


class BoClasse():
    def __init__(self):
        self.dao = GenericDao()

    def create(self, model: Classe):
        return self.dao.create(model)

    def update(self, model: Classe):
        return self.dao.update(model)

    def delete(self, model: Classe):
        return self.dao.delete(model)

    def selectAll(self, model: Classe):
        return self.dao.selectAll(model)
