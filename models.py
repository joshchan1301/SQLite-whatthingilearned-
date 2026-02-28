from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String)

    # Quan hệ: Một User thì có nhiều Posts
    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    # Khóa ngoại liên kết với users.
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Quan hệ ngược lại: Post này thuộc về ai ?
    owner = relationship("User", back_populates="posts")
