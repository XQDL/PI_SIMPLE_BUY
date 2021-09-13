from models.OrdemFornecimento import OrdemFornecimento
from dao.GenericDao import GenericDao



class BoOrdemFornecimento():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: OrdemFornecimento):
                return self.dao.create(model)

        def update(self, model: OrdemFornecimento):
                return self.dao.update(model)

        def delete(self, model: OrdemFornecimento):
                return self.dao.delete(model)

        def selectAll(self, model: OrdemFornecimento):
                return self.dao.selectAll(model)
