# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criação do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = 'sqlite:///database.db'

# Criando a engine e a sessão
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Configuração da sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declaração da base de dados
Base = declarative_base()

# Função para obter a base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()