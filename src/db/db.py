from sqlmodel import create_engine

from ..settings import appsettings

engine = create_engine(appsettings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
