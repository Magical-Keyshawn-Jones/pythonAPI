# from cgitb import text
# from lib2to3.pytree import Base
# from .database import base
# from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.sql.sqltypes import TIMESTAMP
# from sqlalchemy.sql.expression import text

# class Video_Games(Base):
#     __tablename__ = "Video_Games"
    
#     id = Column(Integer, primary_key = True, nullable = False)
#     title = Column(String, nullable = False)
#     rating = Column(Integer, nullable = False, server_default = 'TRUE')
#     preOrdered = Column(Boolean, nullable = True)
#     comment = Column(String, nullable = False)
#     excitement = Column(String, nullable = False)
#     platform = Column(String, nullable = True, server_default = 'TRUE')
#     data_created = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))