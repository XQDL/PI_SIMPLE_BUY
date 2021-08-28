import peewee


class GenericDao:

    def create(self, model):
        return model.save()

    def update(self, model):
        return model.save()

    def delete(self, model):
        return model.delete_instance()

    def selectAll(self, model):
        list = []
        for i in model.select():
            list.append(i)
        return list