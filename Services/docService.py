from Services.Db import Db


class DocService:
    def __init__(self, db : Db) -> None:
        self.db = db
        
        
    def get_doc_patients(self, doc_guid):
        patients = self.db.getData('''
                                    SELECT p.Id, p.Surname, p.Name, p.Midname FROM "Patient" p WHERE DoctorGuid = %s
                                    ''', (doc_guid,))
        return patients