# database.py
# This file sets up the database connection using SQLAlchemy ORM.
# SQLAlchemy is a powerful Python library that lets you interact with
# a SQL database using Python objects instead of raw SQL queries.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The database URL tells SQLAlchemy where the database lives.
# We're using SQLite here — a lightweight, file-based database.
# The file 'blog.db' will be created automatically in the project root.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# create_engine() establishes the connection to the database.
# 'check_same_thread=False' is required for SQLite when used with FastAPI
# because FastAPI can handle multiple threads simultaneously.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# SessionLocal is a factory for creating new database sessions.
# Each request gets its own session, which is used to run queries.
# autocommit=False means changes are not saved until we explicitly call db.commit().
# autoflush=False means SQLAlchemy won't auto-send pending changes to the DB before queries.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base is the parent class that all our ORM models (tables) will inherit from.
# SQLAlchemy uses it to track all the model classes and create tables in the DB.
Base = declarative_base()