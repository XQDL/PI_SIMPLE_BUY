from .GenericDao import GenericDao


class DaoItem(GenericDao):
    def filter(self, Model, id="", desc="", classe="", unidade_medida=""):
        try:
            # if id != "":
            #     models = Model.objects.all().filter(id=id)
            # if desc != "":
            #     models = models.filter(descricao=desc)
            if classe != "":
                models = Model.objects.all().filter(classe=classe)
            # if unidade_medida != "":
            #     models = models.filter(unidadeMedida=unidade_medida)

        except:
            raise
        return models