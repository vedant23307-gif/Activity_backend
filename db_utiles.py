from sqlalchemy import Column,String,Integer,ForeignKey,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import json
engine=create_engine("sqlite:///https.db")
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()
Base.metadata.create_all(engine)
class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,nullable=False)
    user_name=Column(String,nullable=False)
    user_email=Column(String,nullable=False)
Base.metadata.create_all(engine)

def db_create(rawdata):
    data=dict(rawdata)
    name = data.get("name")
    email = data.get("email")
    user = User(user_name=name, user_email=email)
    session.add(user)
    session.commit()
    return "done"



