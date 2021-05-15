# Flask CLI Data Manipulata Language and Data Definition Language Project

The aim of the project is to perform ddl and dml operations on the database with flask cli commands. 


## Install
First, we define the FLASK_APP variable with the following command by giving the path

export FLASK_APP=/path/to/flask_ddl/app.py 

After that, you need to install postgreSQL and pgadmini on your computer via the link below. 

https://codingpub.dev/ubuntu-install-postgresql-and-pgadmin/

Then you need to install pip packages. You can install it with the help of the command below. 

pip3 install -r requirments.txt

After completing the installation process, we can easily do DML and DDL operations on flask-cli. 

I would like to mention that the structure of the database consists of id, job_code, job_description and status. job_code and job_Description are defined as varchar. The status is defined as the boolean parameter. 

## Usage

In order to use Flask Cli, it is necessary to write one of the defined commands after writing Flask. If the relevant command takes any parameter, it is necessary to leave a space and give the parameter. 

### Create a job table 

flask create_table

### Deleting Job Table

flask drop_table

### Insert New Record Job Table 
flask insert JOB_CODE JOB_DESCRIPTION STATUS
flask insert sl001 sales_manager true

### Update  Record Job Table 
flask update JOB_ID JOB_CODE JOB_DESCRIPTION STATUS
flask update 1 hr001 "hr_manager " false

### Update Status Of The Row  Job Table
Job table status guncellemek için
flask update JOB_ID STATUS
flask update 2  true


### List All Record Job Table 
Job table bütün kayıtları getirmek için

flask list

### List  Record By filter Job Table 
flask filter_list STATUS
flask filter_list true

flask filter_list JOB_CODE
flask filter_list hr001


### Removed Row Job Table 
flask remove JOB_CODE
flask remove hr001
