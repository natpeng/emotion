from database import engine

User.__table__
Table('user', MetaData(engine),
    Column('uid', String(32), primary_key=True, nullable=False),
    Column('name', String(32)), schema=None)

Emotion.__table__
Table('emotion', MetaData(engine),
    Column('id', Integer(), primary_key=True, nullable=False),
    Column('uid', String(32)),
    Column('date', String(10)),
    Column('timestamp', String(32)),
    Column('rating', Integer()), schema=None)