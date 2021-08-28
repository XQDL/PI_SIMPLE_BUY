from models import BaseModel as model
import peewee as pw
from models.Item import Item
from models.NotaFiscal import NotaFiscal


class ItemNf(model.BaseModel):
        ItemId = pw.ForeignKeyField(Item)
        NfId = pw.ForeignKeyField(NotaFiscal)
        quantidade = pw.FloatField()
        valorUnitario = pw.FloatField()