import psycopg2

class Db:
    #получение объекта соединения по статическим данным (назв. бд, польз, пароль, хост)
    def getConnection(self):
        return psycopg2.connect(dbname = self.dbname, user = self.user, password = self.psw, host = self.host) 
    #статическое поле объекта данного класса (Singleton)
    unit = None
    
    #выполнение запроса с указанными парараметрами
    def execute(self, sql, params = None):
        with self.getConnection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, params)
    #получение всех данных запроса
    def getData(self, sql, params = None):
        with self.getConnection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, params)
                data = curr.fetchall()
        return data
    #получение первой записи запроса
    def getFirst(self, sql, params = None):
        with self.getConnection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, params)
                data = curr.fetchone()
        return data

    def __init__(self, dbname, user, psw, host = 'localhost') -> None:
        self.dbname = dbname
        self.user = user
        self.psw = psw
        self.host = host
        Db.unit = self