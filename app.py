
# It is the main class from which Flask is started and the incoming cli commands are directed. 
# Author: Selçuk Ildem 

import click
import database
from utils.utils import *
from flask import Flask 
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from containers import Configs,Clients, Managers
import os

Configs.config.override({
    'SQLALCHEMY_DATABASE_URI': 'postgresql://postgres:postgres@localhost:5432/postgres',
})

# configure logging
logger = set_logger( __name__, __file__ )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Configs.config.get("SQLALCHEMY_DATABASE_URI")

database.init_app(app)

# Start listening events
client = Clients.client(database)
object_manager = Managers.object_manager()





@click.command(name='create_table')
@with_appcontext
def create_table():
    logger.info("Creating Job Table")
    object_manager.job.create()




@click.command('drop_table')
@with_appcontext
def drop_table():
    logger.info("Deleting Job Table")
    object_manager.job.drop_table()    
   

@click.command(name='insert')
@with_appcontext
@click.argument('job_code')
@click.argument('job_description')
@click.argument('status')
def insert(job_code,job_description,status):
    logger.info("inserting new row job Table")
    object_manager.job.insert(job_code,job_description,click.BOOL(status))


@click.command('list')
@with_appcontext
def list():
    logger.info("Showing Rows Listed All Record Job Table")
    object_manager.job.list_all()


@click.command('filter_list')
@with_appcontext
@click.argument('filter')
def filter_list(filter):
    logger.info("Showing Rows Listed By Filter Job Table")
    if filter.lower() in ("t","f","true","false"):
       filter=click.BOOL(filter)

    object_manager.job.filter_list(filter)


@click.command('update')
@click.argument('id')
@click.argument('job_code')
@click.argument('job_description')
@click.argument('status')
@with_appcontext
def update(id,job_code,job_description,status):
    logger.info("Updating Row Job Table")
    jobs = object_manager.job.update_status(id,job_code,job_description,click.BOOL(status))


@click.command('update_status')
@click.argument('id')
@click.argument('status')
@with_appcontext
def update_status(id,status):
    logger.info("Updating Status Of The Line  Job Table")
    object_manager.job.update_status(id,click.BOOL(status))




@click.command('remove')
@click.argument('job_code')
@with_appcontext
def remove(job_code):
    logger.info("Removing Status Of The Line  Job Table")
    object_manager.job.remove(job_code)


 
    
#Adding to define cli commands 
app.cli.add_command(create_table)
app.cli.add_command(drop_table)
app.cli.add_command(insert)
app.cli.add_command(remove)
app.cli.add_command(list)
app.cli.add_command(filter_list)
app.cli.add_command(update)
app.cli.add_command(update_status)


