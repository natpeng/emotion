class Emotion(Base):
    __tablename__ = 'emotion'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    uid = Column(String)
    date = Column(String)
    rating = Column(Integer)

Emotion.__table__
Table('emotion', MetaData(engine),
    Column('id', Integer(), primary_key=True, nullable=False),
    Column('uid', String(10)),
    Column('date', String(8)),
    Column('rating', Integer()), schema=None)