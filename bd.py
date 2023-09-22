import sqlalchemy as db 

#engine = db.create_engine("sqlite:///1tdss.db")
engine = db.create_engine("sqlite:///Users/Gabriel/Documents/sqlite-tools-win32-x86-3430100/1tdss.db")
#engine = db.create_engine("sqlite:///C:\\SQlite3\\1tdss.db")

connect = engine.connect()
metadata = db.MetaData()
aluno = db.Table("alunos", metadata, autoload=True, autoload_with=engine)
print(aluno._columns.keys())