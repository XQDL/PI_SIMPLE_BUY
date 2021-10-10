from .GenericDao import GenericDao


class DaoComprador(GenericDao):
    def get_compradores_by_empresa(self, Model, empresa):
        try:
            models = Model.objects.all().filter(empresa=empresa)
        except:
            raise
        return models