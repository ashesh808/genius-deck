from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    registered_on = Column(DateTime, nullable=False)

class UploadedMaterialModel(Base):
    __tablename__ = 'uploaded_material'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    date_uploaded = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class FlashCardModel(Base):
    __tablename__ = 'flash_cards'
    id = Column(Integer, primary_key=True)
    uploaded_material_id = Column(Integer, ForeignKey('uploaded_material.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    generation_date = Column(DateTime, nullable=False)
    is_private = Column(Boolean, nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    generation_model = Column(String(100), nullable=False)

class TagModel(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

class LoginSessionModel(Base):
    __tablename__ = 'login_session'
    id = Column(Integer, primary_key=True)
    logged_in_date = Column(DateTime, nullable=False)
    auth_token = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)