import peewee


class GenericDao:

    def create(self, model):
        try:
            return model.save()
        except:
            return 'Erro ao Salvar'


    def update(self, model):
        try:
            return model.save()
        except:
            return 'Erro ao Salvar'


    def delete(self, model):
        return model.delete_instance()

    def selectAll(self, model):
        list = []
        for i in model.select():
            list.append(i)
        return list