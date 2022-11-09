from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(70), unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

class Post(Base):

    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    text = Column(String(500), unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.title,
            "email": self.text
        }

