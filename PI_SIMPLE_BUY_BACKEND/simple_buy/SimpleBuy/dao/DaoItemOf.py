from .GenericDao import GenericDao
from ..models import Itens_of

class DaoItemOf(GenericDao):
    def get_itens_by_of(self, of):
        try:
            ofs = Itens_of.objects.all().filter(num_of=of)
        except:
            raise
        return ofs

    def get_valor_aproximado(self, item):
        try:
            itens = Itens_of.objects.all().filter(cod_item=item).order_by('dataEntrega')

        except:
            raise
        return itens[0].valor_unitario

