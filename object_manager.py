#
#  Object manager is the core component of the master module. Object manager also controls all execution operations.
#
#Author: Selçuk Ildem 

import sys
import traceback
import logging
from utils import utils


class ObjectManager:

    def __init__(self, client):
        # Get logger
        self._logger = utils.get_logger()
        self._logger.setLevel(logging.DEBUG)
        self._client = client


    # Database DDL and DML  operation manager
    @property
    def job(self):
        return JobManager(ddl_client=self._client, logger=self._logger)






class JobManager:
    """
    Object manager uses this class as a property.
    All DDL operations executed by  client is responsibility of the job manager.
    """
 
    def __init__(self, ddl_client, logger):
        self._client = ddl_client
        self._logger = logger

    def get(self, service_id):
        try:
            self._client.job.get(service_id)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)


    def create(self):
        try:
            self._client.job.create()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    

    def insert(self,job_code,job_description,status):
        try:
            self._client.job.insert(job_code,job_description,status)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    

    def remove(self,job_code):
        try:    
            self._client.job.remove(job_code)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    
    def drop_table(self):
        try:
            self._client.job.drop_table()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)

    def list_all(self):
        try:
            self._client.job.list_all()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    
    def filter_list(self,filter):
        try:
            self._client.job.filter_list(filter)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    def update(self,id,job_code,job_description,status):
        try:
            self._client.job.update(id,job_code,job_description,status)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
    def update_status(self,id,status):
        try:
            self._client.job.update_status(id,status)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error("*** tb_lineno:", exc_traceback.tb_lineno)
   


