from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float

class Dog(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)

engine = create_engine('mysql://root:mypassword@data-bootcamp-rutgers.cn6jzamkgcqr.us-west-2.rds.amazonaws.com:3306/pets')
conn = engine.connect()
Base.metadata.create_all(conn)

from sqlalchemy.orm import Session
session = Session(bind=engine)

# Create a query and then run update on it
dog = session.query(Dog).filter_by(name="Fido").first()
dog.age += 1
session.commit()

# Create a query and then delete the row collected
dog = session.query(Dog).filter_by(id==1).delete()
session.commit()