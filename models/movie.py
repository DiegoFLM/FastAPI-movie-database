from config.database import Base
from sqlalchemy import Column, Integer, String, Float

# Movie hineritates from Base, which is a class from SQLAlchemy
# Base is a class that is used to create a table in the database
class Movie(Base):
    __tablename__ = 'movies'    

    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)

