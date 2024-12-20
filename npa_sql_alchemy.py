import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("sqlite:///european_database.sqlite")
metadata = db.MetaData()

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "ca_name"

    user_name = Column(String, primary_key=True)
    safe_id = Column(Integer)
    safe_name = Column(String)

# DEFINE THE DATABASE CREDENTIALS
user = 'zbtools'
password = 'D0br0!74p@ny'
host = 'accengdbprod.c9pxjgrv7vhh.us-east-1.rds.amazonaws.com'
port = 3306
database = 'metatools_db'
 
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    #engine = create_engine(f"mysql:///?User={user}&Password={password}&Database={database}&#erver={host}&Port=3306")
    #return engine
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
    )

try:
    # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
    engine = get_connection()
    print(f"Connection to the {host} for user {user} created successfully.")
except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)

# query something in cyberar names 
statement = text("""SELECT Name FROM ca_name WHERE safe_name = 'LNX_Root_POC'""")
conn = engine.connect() 

factory = sessionmaker(bind=engine)
session = factory()

output = session.execute(statement, [])
print(output.fetchall())