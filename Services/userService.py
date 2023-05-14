from Services.Db import Db


class UserService:
    
    unit = None
    
    def __init__(self, db) -> None:
        self.db = db
        self.exit()
        UserService.unit = self
        
    def setUser(self, guid, name, role) -> None:
        self.guid = guid
        self.name = name
        self.role = role
        self.isAutent = True

    def getUserGuid(self) -> None | str:
        return self.guid

    def getUser(self) -> None | tuple:
        if self.isAutent:
            return self.guid, self.name, self.role
        return None
    
    def IsAutent(self) -> bool:
        return self.isAutent
    
    def exit(self):
        self.isAutent = False
        self.name = None
        self.guid = None
        self.role = None