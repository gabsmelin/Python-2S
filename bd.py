import sqlalchemy as db 

engine = db.create_engine("sqlite:///1tdss.db")
#engine = db.create_engine("sqlite:///Users/Gabriel/Documents/sqlite-tools-win32-x86-3430100/1tdss.db")
#engine = db.create_engine("sqlite:///C:\\SQlite3\\1tdss.db")

connect = engine.connect()
metadata = db.MetaData()
aluno = db.Table("alunos", metadata, autoload_with=engine)
print(aluno.columns.keys())

#emp = db.Table("alunos", metadata, 
#            db.Column("id", db.Integer()),
#            db.Column("name", db.Text()),
#            db.Column("turma", db.Text()),
#            db.Column("obs", db.Text()))
#
#jog = db.Table()
#metadata.create_all(engine)

query = db.insert(aluno).values(id=1, name="Gabriel", turma="1TDSS", obs='Lindo')
ResultProxy = connect.execute(query)

resultado = connect.execute(db.select([aluno])).fetchall()
print(resultado)