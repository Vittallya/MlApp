
from uuid import uuid4
from math import ceil, floor
from werkzeug.security import generate_password_hash

class EmployeeService:
    def __init__(self, db) -> None:
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
            
    def check_login(self, uuid, login):
        
        query = '''SELECT COUNT(*) FROM EmployeeUser u WHERE u.Login = %s'''
        params = (login,)
        
        if uuid != None:
            query += ' AND u.Id <> %s'
            params = params + (uuid,)
        
        return self.db.getFirst(query, params)[0]
    
    def add_or_edit_employee(self, uuid, name, surname, midname, phone, date_start, posId, restId):
        
        if uuid == None:
            uuid = uuid4().hex
            self.db.execute('''INSERT INTO Employee 
                            (Id, Name, Surname, Midname, StartWorkDate, Phone, PositionId, RestoranId) VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s)''', 
                            (uuid, name, surname, midname, date_start, phone, int(posId), int(restId)))
        else:
            self.db.execute('''UPDATE Employee e SET Name = %s, Surname = %s, Midname = %s,
                            StartWorkDate = %s, Phone = %s, PositionId = %s, RestoranId = %s
                            WHERE e.Id = %s''', 
                            (name, surname, midname, date_start, phone, int(posId), int(restId), uuid))
        
        return uuid
        
                
        
        