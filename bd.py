import sqlalchemy as db

engine = db.create_engine("sqlite:///1tdss.db")


connect = engine.connect()
metadata = db.MetaData()
metadata.bind = engine
metadata.reflect(bind=engine)

aluno = db.Table('aluno', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('nome', db.String), db.Column('turma', db.String), db.Column('obs', db.String))

metadata.create_all(engine)
print(aluno.columns.keys())


#aluno = db.Table("alunos", metadata,
#    db.Column("id", db.Integer),
#    db.Column("turma", db.String),
#    db.Column("name", db.String),
#    db.Column("obs", db.String)
#)
#
#print(aluno.columns.keys())
#
#values = {
#    "id": 1,
#    "turma": "1tdss",
#    "name": "melo",
#    "obs": 'lindo'
#}
#
#query = db.insert(aluno).values(**values)
#ResultProxy = connect.execute(query)
#
#select_query = db.select(aluno)
#resultado = connect.execute(select_query).fetchall()
#
#print(resultado)
