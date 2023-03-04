from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DummyTestDB(Base):
    """
    This model is used only for testing purposes
    """

    __tablename__ = "dummy"

    id = Column(Integer, primary_key=True)
    attribute = Column(String(20), nullable=False, unique=True)



class FilmeDB(Base):
    """
    This model is used only for testing purposes
    """

    __tablename__ = "filme"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    director = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Filme(title='{self.title}', director='{self.director}')>"