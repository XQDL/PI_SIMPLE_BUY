from .GenericDao import GenericDao


class DaoEmpresaCompradora(GenericDao):
    def get_empresa_by_adm(self, Model, adm):
        try:
            empresa = Model.objects.get(administrador=adm)
        except:
            raise
        return empresa