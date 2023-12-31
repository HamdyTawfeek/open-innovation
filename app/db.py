from os import environ
from sqlalchemy import create_engine

engine = create_engine(
    environ.get('SQLALCHEMY_DATABASE_URI')
    )
