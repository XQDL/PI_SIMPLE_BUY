from models.NotaFiscal import NotaFiscal
from dao.GenericDao import GenericDao


class BoNotaFiscal():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: NotaFiscal):
                return self.dao.create(model)

        def update(self, model: NotaFiscal):
                return self.dao.update(model)

        def delete(self, model: NotaFiscal):
                return self.dao.delete(model)

        def selectAll(self, model: NotaFiscal):
                return self.dao.selectAll(model)
