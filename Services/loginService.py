from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
#from Services.Db import Db

class LoginService:
    
    def __init__(self, db) -> None:
        self.db = db
    
    
    def tryAuthentificate(self, login, password):
        user_start = self.db.getFirst('''   SELECT e.PasswordHash, e.Guid, r.Guid, r.Name, e.Login, e.Name FROM "Employee" e
                                            INNER JOIN "Role" r on r.Guid = e.RoleGuid
                                            WHERE  e.Login = %s ''', (login,))
        
        if user_start == None or not check_password_hash(user_start[0], password):
            return None
        
        usr = list(user_start)
        usr.pop(0)
        return tuple(usr)
        