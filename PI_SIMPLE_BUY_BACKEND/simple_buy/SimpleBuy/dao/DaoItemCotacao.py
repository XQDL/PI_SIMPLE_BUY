from ..models import Comprador
from .GenericDao import GenericDao
from .DaoComprador import DaoComprador

class DaoItemCotacao(GenericDao):
    def select_by_empresa(self, Model, empresa):

        try:

            models = Model.objects.all()



            dao = DaoComprador()

            compradores = dao.get_compradores_by_empresa(Comprador, empresa)



            lista_definitiva = []

            itens_solicitados_adm = models.filter(solicitante_adm=empresa.administrador)

            if itens_solicitados_adm:
                for item in itens_solicitados_adm:
                    lista_definitiva.append(item)

            for comprador in compradores:
                temp = models.filter(solicitante_comprador=comprador)
                if temp:
                    for item in temp:
                        lista_definitiva.append(item)


        except:
            raise
        return lista_definitiva