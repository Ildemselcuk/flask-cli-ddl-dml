# It is the class that DDL and DML operations are performed on the database with extended methods. 

#Author: Selçuk Ildem 


import sys
import traceback
import logging
from model import Job
from utils import utils



class Client:

    def __init__(self,db):
        # Get logger
        self.logger = logging.getLogger(self.__class__.__name__)
        # Set logging level to logging.DEBUG if you want to debug client
        self.logger.setLevel(logging.ERROR)
        self.database =db


    # Database DDL and DML operations
    @property
    def job(self):
        return JobService(client=self)


class JobService:
    def __init__(self, client):
        self._client = client
        self.database = client.database
        self.logger = utils.get_logger()
        # Set logging level to logging.DEBUG if you want to debug client
        self.logger.setLevel(logging.DEBUG)

  
    # Creates a new service with given parameters
    def create(self):#limit
        try:
            self.database.db.create_all()
            self.database.db.session.commit()
            self.logger.info("Created Job Table")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    
    def drop_table(self):
        try:
            Job.__table__.drop(self.database.db.engine)
            self.database.db.session.commit()
            self.logger.info("Deleted  Job Table")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)

    def insert(self,job_code,job_description,status):
        try:
            new_job = Job(job_code, job_description,status)
            self.database.db.session.add(new_job)
            self.database.db.session.commit()
            self.logger.info("Inserted new record Job Table")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)

    def remove(self,code):
        try:
            first_job = Job.query.filter_by(job_code = code).first()

            delete_row=Job.query.filter_by(id = first_job.id).delete()
            self.database.db.session.commit()
            self.logger.info("Removed Row Job Table")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    

    def list_all(self):
        try:
            list_job = Job.query.all()
            print("JOB ID"+"  "+"JOB CODE"+" "+"JOB DESCRIPTION"+" "+"STATUS")
            for list in list_job:
                print("   "+str(list.id)+"    "+str(list.job_code)+"    "+str(list.job_description)+"    "+str(list.status))
            self.logger.info("Showed List of All Record  Job Table")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    
    def filter_list(self,filter):
        try:
            if isinstance(filter, str):
                list_job = Job.query.filter_by(job_code =filter).all()
            elif isinstance(filter, bool):
                print("Gelen Filtre "+str(filter))
                list_job = Job.query.filter_by(status =filter).all()
            print("JOB ID"+"  "+"JOB CODE"+" "+"JOB DESCRIPTION"+" "+"STATUS")
            for list in list_job:
                print("   "+str(list.id)+"    "+str(list.job_code)+"    "+str(list.job_description)+"    "+str(list.status))
            self.logger.info("Showed Rows Listed By Filter Job Table")

        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)

    def update(self,id=None,jobCode=None,jobDescription=None,status=None):
        try:
            if id != None:
                edit_job = Job.query.filter_by(id = id).first()
                edit_job.job_code = jobCode
                edit_job.job_description = jobDescription
                edit_job.status = status
            elif jobCode != None:
                edit_job = Job.query.filter_by(job_code = jobCode).first()
                edit_job.job_description = jobDescription
                edit_job.status = status
                
            self.database.db.session.commit()
            self.logger.info("Updated Row Job Table")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    
    def update_status(self,id,status):
        try:
            edit_job = Job.query.filter_by(id = id).first()
            edit_job.status = status
            self.database.db.session.commit()
            self.logger.info("Updated Status Of The Line  Job Table")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)

          
