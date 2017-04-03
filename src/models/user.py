from src.common.database import Database

class user(object):
    """ Let user log in, register and stuff like that"""

    def __init__(self,email,password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users",{"email":email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users",{"_id":id})
        if data is not None:
            return cls(**data)
        return None #default return

    def login_valid(self,email):
        #Check whether user's email matches the password they sent us
        user = User.get_by_email(email)

    def register(self):
        pass

    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        pass