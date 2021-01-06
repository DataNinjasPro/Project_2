# Import SQL Alchemy
from sqlalchemy import create_engine

# Import PyMySQL (Not needed if mysqlclient is installed)
import pymysql
pymysql.install_as_MySQLdb()

# Import and establish Base for which classes will be constructed
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float

# Create Surfer and Board classes
# ----------------------------------
class Surfer(Base):
    __tablename__ = 'surfers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    hometown = Column(String(255))
    wipeouts = Column(Integer)
    rank = Column(Integer)

class Board(Base):
    __tablename__ = 'surfboards'
    id = Column(Integer, primary_key=True)
    surfer_id = Column(Integer)
    board_name = Column(String(255))
    color = Column(String(255))
    length = Column(Integer)

# Create specific instances of the Surfer and Board classes
# ----------------------------------
# Create a new surfer named "Bruno"
surfer = Surfer(id=1, name='Bruno', hometown="LA", wipeouts=1, rank=10)
# Create a new board and associate it with a surfer's ID
board = Board(id=1, surfer_id=1, board_name="Awwwyeah", color="Blue", length=68)

# Create Database Connection
# ----------------------------------
# Establish Connection to MySQL
engine = create_engine('mysql://root:<password>@localhost:3306/surfingdb')

# Create both the Surfer and Board tables within the database
Base.metadata.create_all(engine)

# To push the objects made and query the server we use a Session object
from sqlalchemy.orm import Session
session = Session(bind=engine)

# Add "Bruno" to the current session
session.add(surfer)
# Add "Awwwyeah" to the current session
session.add(board)
# Commit both objects to the database
session.commit()

# Query the database and collect all of the surfers in the Surfer table
surfer_list = session.query(Surfer)
for bro in surfer_list:
    print(bro.name)
    print(bro.hometown)
    print(bro.wipeouts)
    print(bro.rank)

# Query the database and collect all of the boards in the Board table
board_list = session.query(Board)
for board in board_list:
    print(board.board_name)
    print(board.color)
    print(board.length)