from models import BaseModel as model
import peewee as pw
from models.Item import Item
from models.OrdemFornecimento import OrdemFornecimento


class ItemOf(model.BaseModel):
        ItemId = pw.ForeignKeyField(Item)
        OfId = pw.ForeignKeyField(OrdemFornecimento)
        quantidade = pw.FloatField()
        valorUnitario = pw.FloatField()
        recebido = pw.FloatField()
        saldo = pw.FloatField()


        