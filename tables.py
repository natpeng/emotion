from database import engine
from sqlalchemy import Table, Column, Integer, String, MetaDta, ForeignKey

metadata = MetaData(engine)

User.__table__
Table('user', metadata,
    Column('uid', String(32), primary_key=True, nullable=False),
    Column('name', String(32)), schema=None)

Emotion.__table__
Table('emotion', metadata,
    Column('id', Integer(), primary_key=True, nullable=False),
    Column('uid', String(32), ForeignKey('user.uid')),
    Column('date', String(10)),
    Column('timestamp', String(32)),
    Column('rating', Integer()), schema=None)

metadata.create_all()