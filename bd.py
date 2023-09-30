import sqlalchemy as db

engine = db.create_engine("sqlite:///1tdss.db")
connect = engine.connect()
metadata = db.MetaData()

# Defina explicitamente a estrutura da tabela "alunos"
aluno = db.Table("alunos", metadata,
    db.Column("id", db.Integer),
    db.Column("turma", db.String),
    db.Column("name", db.String),
    db.Column("obs", db.String)
)

print(aluno.columns.keys())

# Crie um dicionário com os valores que deseja inserir
values = {
    "id": 1,
    "turma": "1tdss",
    "name": "melo",
    "obs": 'lindo'
}

# Crie a consulta de inserção com os valores
query = db.insert(aluno).values(**values)
ResultProxy = connect.execute(query)

# Corrija a consulta SELECT para selecionar todas as colunas da tabela "alunos"
select_query = db.select(aluno)
resultado = connect.execute(select_query).fetchall()

print(resultado)
