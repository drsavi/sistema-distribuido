from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FilmeDB(Base):

    __tablename__ = "filme"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    director = Column(String(100), nullable=False)
    duration = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Filme(title='{self.title}', director='{self.director}',director='{self.director}')>"