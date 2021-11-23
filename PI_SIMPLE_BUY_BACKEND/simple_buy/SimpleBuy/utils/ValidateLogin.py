from ..dao.GenericDao import GenericDao
from ..dao.DaoLogin import DaoLogin


class ValidadeLogin():
    def __init__(self):
        self.dao = DaoLogin()


    def validate_and_get_context(self, user, password):
        try:
            user = self.dao.validate_login(user, password)
            context = {
                "user": user
            }
        except:
            context = {
                "err": "invalid login"
            }

        return context