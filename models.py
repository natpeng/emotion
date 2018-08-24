from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UserModel(Base):
    __tablename__ = 'user'
    uid = Column(String, primary_key=True)
    name = Column(String)

class EmotionModel(Base):
    __tablename__ = 'emotion'
    id = Column(Integer, primary_key=True)
    uid = Column(ForeignKey('user.uid'))
    timestamp = Column(String)
    date = Column(String)
    rating = Column(Integer)
    
Base.prepare(engine)