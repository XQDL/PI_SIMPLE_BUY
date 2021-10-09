class GenericDao:

    def create(self, model):
        try:
           model.save()
        except:
            raise

        return model


    def update(self, model):
        try:
             model.save()
        except:
             raise
        return model

    def delete(self, Model, id):
        return Model.exclude(id=id)

    def selectAll(self, Model):
        list = []
        for i in Model.objects.all():
            list.append(i)
        return list


    def get(self, Model, id):
        try:
            model = Model.objects.get(id=id)
        except:
            raise
        return model