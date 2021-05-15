
#It is the class in which the table and columns we will create in the database are defined. 
#In this class, its columns can be defined as unique, primary_key, foreign_key. 
# In addition, limits can be added to data types. 
# Author: Selçuk Ildem 

from database import db

class Job(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    job_code = db.Column(db.String(100))
    job_description = db.Column(db.String(50))  
    status = db.Column(db.Boolean)

    def __init__(self, job_code, job_description, status):
        self.job_code = job_code
        self.job_description = job_description
        self.status = status
