from datetime import datetime

from sqlalchemy import Column, Integer, String
from tornado_sqlalchemy import SQLAlchemy

# Base = declarative_base()
# define('database_url',default='postgresql://postgres:1234@localhost:5432/postgres', help="database")

database_url = 'postgresql://postgres:1234@localhost/postgres'
db = SQLAlchemy(url=database_url)


class UserModel(db.Model):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)