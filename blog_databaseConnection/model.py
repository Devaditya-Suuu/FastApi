# model.py
# This file defines the database table structure using SQLAlchemy ORM models.
# Each Python class here maps to a table in the database.
# Each class attribute maps to a column in that table.

from .database import Base
from sqlalchemy import Column, Integer, String

# The Blog class represents the 'blogs' table in the SQLite database.
# It inherits from Base so SQLAlchemy knows to treat it as a database model.
class Blog(Base):
    # __tablename__ tells SQLAlchemy what to name the table in the database.
    __tablename__ = 'blogs'

    # 'id' is the primary key — a unique auto-incrementing integer for each blog post.
    # index=True creates a database index on this column for faster lookups.
    id = Column(Integer, primary_key=True, index=True)

    # 'title' stores the heading/title of the blog post as a string.
    title = Column(String)

    # 'body' stores the main content/text of the blog post.
    body = Column(String)