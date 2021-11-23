from .GenericDao import GenericDao
from ..models import Administrador, Comprador


class DaoLogin(GenericDao):
    def validate_login(self, user, password):
        try:
            model = Administrador.objects.get(nomeUsuario=user, senha=password)

            return model
        except:
            try:
                model = Comprador.objects.get(nomeUsuario=user, senha=password)

                return model
            except:
                raise Exception('Invalid Login')
