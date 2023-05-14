from Services.Db import Db


class DocService:
    def __init__(self, db : Db) -> None:
        self.db = db
        
        
    def get_doc_patients(self, doc_guid):
        patients = self.db.getData('''SELECT * FROM "Patient" WHERE DoctorGuid = %s''', (doc_guid,))
        return patients