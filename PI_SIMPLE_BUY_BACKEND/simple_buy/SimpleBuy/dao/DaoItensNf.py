from .GenericDao import GenericDao
from ..models import Itens_nf

class DaoItemNf(GenericDao):
    def get_itens_by_nf(self, nf):
        try:
            ofs = Itens_nf.objects.all().filter(num_nf=nf)
        except:
            raise
        return ofs
