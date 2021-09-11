from models.ClasseFornecedor import ClasseFornecedor
from dao.GenericDao import GenericDao


class BoClasseFornecedor():
    def __init__(self):
        self.dao = GenericDao()

    def create(self, model: ClasseFornecedor):
        return self.dao.create(model)

    def update(self, model: ClasseFornecedor):
        return self.dao.update(model)

    def delete(self, model: ClasseFornecedor):
        return self.dao.delete(model)

    def selectAll(self, model: ClasseFornecedor):
        return self.dao.selectAll(model)
