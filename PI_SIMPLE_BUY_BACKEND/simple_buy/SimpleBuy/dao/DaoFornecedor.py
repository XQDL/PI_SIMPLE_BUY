from .GenericDao import GenericDao
from ..models import Fornecedor

class DaoFornecedor(GenericDao):
    def get_fornecedor_by_classe(self, classe):
        try:
            fornecedores = Fornecedor.objects.all().filter(classe=classe)
        except:
            raise
        return fornecedores
