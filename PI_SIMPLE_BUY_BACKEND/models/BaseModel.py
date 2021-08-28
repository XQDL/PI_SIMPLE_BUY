import peewee

# Criamos o banco de dados
db = peewee.SqliteDatabase('teste.db')

class BaseModel(peewee.Model):
    """Classe model base"""
    class Meta:
        database = db

