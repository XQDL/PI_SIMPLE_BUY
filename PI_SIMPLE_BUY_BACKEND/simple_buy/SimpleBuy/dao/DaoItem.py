from .GenericDao import GenericDao


class DaoItem(GenericDao):
    def filter(self, Model, id="", desc="", classe="", unidade_medida=""):
        try:

            models = Model.objects.all()

            if id != "":
                models = models.filter(id=id)
            if desc != "":
                models = models.filter(descricao__contains=desc)
            if classe != "":
                models = models.filter(classe=classe)
            if unidade_medida != "":
                models = models.filter(unidadeMedida=unidade_medida)

        except:
            raise
        return models