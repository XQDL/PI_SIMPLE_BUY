from ..dao.GenericDao import GenericDao
from ..models import Administrador, Comprador


class Profile_validate:
    def verify_existing_profile(self, username):
        dao = GenericDao()
        adm = None
        comprador = None

        print(username)

        try:
            adm = dao.get_by_username(Administrador, username)
        except:
           print('Errado')
        try:
            comprador = dao.get_by_username(Comprador, username)
        except:
           print('Errado')




        if adm != None or comprador != None:
            print('SIM')
            return True
        else:
            print('NÃO')
            return False





