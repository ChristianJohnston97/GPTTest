from sqlalchemy import create_engine
import pandas as pds
import random

def construct_postgres_connection():
    alchemy_engine = create_engine('postgresql+psycopg2://postgres:@localhost/database', pool_recycle=3600)
    db_connection = alchemy_engine.connect()
    return db_connection

def closeConnection(db_connection):
    db_connection.close()

def getAllSegments(db_connection):
    data_frame = pds.read_sql("select * from segments", db_connection)
    return data_frame
