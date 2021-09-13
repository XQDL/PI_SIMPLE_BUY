from models.EmpresaCompradora import EmpresaCompradora
from dao.GenericDao import GenericDao


class BoEmpresaCompradora():
        def __init__(self):
                self.dao = GenericDao()

        def create(self, model: EmpresaCompradora):
                return self.dao.create(model)

        def update(self, model: EmpresaCompradora):
                return self.dao.update(model)

        def delete(self, model: EmpresaCompradora):
                return self.dao.delete(model)

        def selectAll(self, model: EmpresaCompradora):
                return self.dao.selectAll(model)
