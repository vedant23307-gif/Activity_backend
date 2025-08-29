from sqlalchemy import Column,ForeignKey,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()
class Person(Base):
    __tablename__="Person"
    id=Column("id",Integer,primary_key=True)
    name=Column("name",String)
    roll=Column("roll",Integer)
     
    def __init__(self,id,name,roll):
        self.id=id
        self.name=name
        self.roll=roll
engine=create_engine("sqlite:///mydatbase.db")
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()
person=Person(20,"vedant",45)
session.add(person)
session.commit()