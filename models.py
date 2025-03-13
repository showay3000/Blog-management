# models.py

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Database setup
DATABASE_URL = "sqlite:///blog.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Base class for ORM models
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    posts = relationship("Post", back_populates="author", cascade="all, delete")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"

# Define Post model
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, author={self.user_id})>"

# Create tables in the database
Base.metadata.create_all(engine)