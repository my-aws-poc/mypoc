from sqlalchemy import Column, BigInteger, String, Integer, DateTime

from mypoc import db


class Pet(db.Model):
    __tablename__ = 'pet'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(45))
    age = Column(Integer)
    created = Column(DateTime)

    def __init__(self, name, age, created=None) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.created = created

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
