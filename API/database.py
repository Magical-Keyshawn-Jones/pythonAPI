from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@ip-address/hostname/<database-name>'
# Never hard this
SQLALCHEMY_DATABASE_URL = 'postgresql://killz:2@localhost/Video_Games'

# Engine establishes the connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()