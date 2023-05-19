
from uuid import uuid4
from math import ceil, floor
from werkzeug.security import generate_password_hash
from Services.Db import Db

class EmployeeService:
    def __init__(self, db:Db) -> None:
        self.db = db  
        

    def getEmployeesTotal(self):
        total = self.db.getFirst('''SELECT COUNT(*) FROM Employee''')[0]
        return str(total)
        
    def getEmployees(self, take, page):
        skip = (page - 1) * take
        emp = self.db.getData('''SELECT e.Id, e.Surname, e.Name, e.Midname, e.StartWorkDate, p.Name, p.Id, u.Id  FROM Employee e
                              INNER JOIN PositionWork p ON p.Id = e.Positionid 
                              LEFT JOIN EmployeeUser u ON u.Id = e.Id LIMIT %s OFFSET %s''', (take, skip))
        return emp
    
    def findEmpById(self, id):
        emp = self.db.getFirst('''SELECT * FROM Employee e WHERE e.Id = %s''', (id,))
        return emp
    
    def delete_emp(self, uuid):
        self.db.execute("DELETE FROM Employee e WHERE e.Id = %s", (uuid,))
    
    def get_user(self, uuid):
        return self.db.getFirst('''SELECT u.Login, u.UserRole FROM EmployeeUser u WHERE u.Id = %s''', (uuid,))
    
    def remove_user(self, uuid):
        self.db.execute('''DELETE FROM EmployeeUser u WHERE u.Id = %s''', (uuid,))
    
    def update_password(self, uuid, password):
        passwd_hash = generate_password_hash(password)
        self.db.execute('''UPDATE EmployeeUser u SET PasswordHash = %s WHERE u.Id = %s''', 
                        (passwd_hash, uuid))
    
    def add_or_edit_user(self, uuid, login, role, acc_level, is_exists):

        if is_exists:
            self.db.execute('''UPDATE EmployeeUser u SET Login = %s, AccessLevel = %s, 
                            UserRole = %s WHERE u.Id = %s''', (login, acc_level, role, uuid))
        else:
            self.db.execute('''INSERT INTO EmployeeUser (Id, Login, AccessLevel, UserRole)
                            VALUES(%s, %s, %s, %s)''', (uuid, login, acc_level, role))
            
    def is_login_exists(self, login) -> bool:
        
        query = '''SELECT COUNT(*) FROM "Employee" e WHERE e.Login = %s'''
        params = (login,)
        req = self.db.getFirst(query, params)
        return req != None and int(req[0]) > 0

    
    def update_emp_without_usr_data(self, guid, name, surname, midname, roleGuid):
        self.db.execute('''UPDATE "Employee" e SET Name = %s, Surname = %s, Midname = %s, RoleGuid = %s
                            WHERE e.Guid = %s''', 
                            (name, surname, midname, roleGuid, guid))
    
    def add_or_edit_employee(self, guid, name, surname, midname, login, password, roleGuid):        
        
        if guid == None:
            guid = uuid4().hex
            self.db.execute('''INSERT INTO "Employee" 
                            (Guid, Name, Surname, Midname, Login, PasswordHash, RoleGuid) VALUES
                            (%s, %s, %s, %s, %s, %s, %s)''', 
                            (guid, name, surname, midname, login, generate_password_hash(password), roleGuid))
        else:
            self.db.execute('''UPDATE "Employee" e SET Name = %s, Surname = %s, Midname = %s,
                            RoleGuid = %s, Login = %s, PasswordHash = %s
                            WHERE e.Guid = %s''', 
                            (name, surname, midname, roleGuid, login, generate_password_hash(password), guid))
        
        return guid
        
                
        
        