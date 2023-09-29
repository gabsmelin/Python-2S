import sqlalchemy as db

#engine = db.create_engine("sqlite:///1tdss.db")
#engine = db.create_engine("sqlite:////absolute/path/to/1tdss.db") 
engine = db.create_engine("sqlite:///X:\\Programação\\FIAP\\2023\\Python\\SQLite") 

metadata = db.MetaData()
aluno = db.Table("alunos", metadata, autoload=True, autoload_with=engine)
print(aluno.columns.keys())
query = db.insert(aluno).values(id=1, name="Alberico", turma="1tdss", obs='nada')
ResultProxy = db.connect.execute(query)

resultado = db.connect.execute(db.select([aluno])).fetchall()
print(resultado)