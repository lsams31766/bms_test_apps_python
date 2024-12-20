import sqlalchemy as db
from sqlalchemy.sql import text

engine = db.create_engine("sqlite:///european_database.sqlite")
metadata = db.MetaData()
Student = db.Table('Student', metadata,
              db.Column('Id', db.Integer(),primary_key=True),
              db.Column('Name', db.String(255), nullable=False),
              db.Column('Major', db.String(255), default="Math"),
              db.Column('Pass', db.Boolean(), default=True)
              )

# metadata.create_all(engine) 
conn = engine.connect() 

#query = db.insert(Student).values(Id=1, Name='Matthew', Major="English", Pass=True)
#Result = conn.execute(query)
#output = conn.execute(Student.select()).fetchall()
#print(output)

query = db.insert(Student)
values_list = [{'Id':'2', 'Name':'Nisha', 'Major':"Science", 'Pass':False},
              {'Id':'3', 'Name':'Natasha', 'Major':"Math", 'Pass':True},
              {'Id':'4', 'Name':'Ben', 'Major':"English", 'Pass':False}]
Result = conn.execute(query,values_list)
#output = conn.execute(Student.select()).fetchall()
#print(output)

statement = text("""SELECT Name FROM Student""")
output = conn.execute(statement, [])
print(output.fetchall())

query = Student.select().where(Student.columns.Major == 'English')
output = conn.execute(query)
print(output.fetchall())

