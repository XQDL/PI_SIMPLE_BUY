from .GenericDao import GenericDao


class DaoLogin(GenericDao):
    def validate_login(self, Model, user, password):
        try:
            model = Model.objects.get(nomeUsuario=user, senha=password)
        except:
            raise
        return model