from .GenericDao import GenericDao
from ..models import OrdemFornecimento
from ..models import Itens_of

class DaoOrdemFornecimento(GenericDao):
    def get_by_fornecedor(self, fornecedor, situacao = 0):
        try:
            model = OrdemFornecimento.objects.all().filter(fornecedor=fornecedor)
            if situacao != 0:
                model = model.filter(situacao = situacao)
        except:
            raise
        return model

    def get_by_situacao(self, situacao):
        try:
            model = OrdemFornecimento.objects.all().filter(situacao=situacao)
        except:
            raise
        return model

    def get_by_fornecedor_situacao_and_item(self, fornecedor, situacao, item):
        try:
            models = OrdemFornecimento.objects.all().filter(fornecedor=fornecedor).filter(situacao=situacao)

            lista_itens_of = []
            for model in models:
                temp_itens = Itens_of.objects.all().filter(num_of=model).filter(cod_item=item)
                for temp_item in temp_itens:
                    lista_itens_of.append(temp_item)

            lista_definitiva = []
            for item_of in lista_itens_of:
                lista_definitiva.append(item_of.num_of)


        except:
            raise
        return lista_definitiva
