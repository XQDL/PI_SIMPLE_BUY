
from models import BaseModel as model
import peewee as pw
from models.OrdemFornecimento import OrdemFornecimento
from models.NotaFiscal import NotaFiscal


class OfNf(model.BaseModel):
        OfId = pw.ForeignKeyField(OrdemFornecimento)
        NfId = pw.ForeignKeyField(NotaFiscal)