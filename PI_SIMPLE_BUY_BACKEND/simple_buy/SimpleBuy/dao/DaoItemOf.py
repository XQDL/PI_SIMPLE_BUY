from .GenericDao import GenericDao
from ..models import Itens_of

class DaoItemOf(GenericDao):
    def get_itens_by_of(self, of):
        try:
            ofs = Itens_of.objects.all().filter(num_of=of)
        except:
            raise
        return ofs
