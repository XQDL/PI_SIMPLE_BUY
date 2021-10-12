from .GenericDao import GenericDao
from ..models import OrdemFornecimento

class DaoOrdemFornecimento(GenericDao):
    def get_by_fornecedor(self, fornecedor):
        try:
            model = OrdemFornecimento.objects.all().filter(fornecedor=fornecedor)
        except:
            raise
        return model