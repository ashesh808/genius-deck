# Entities
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    registered_on: datetime

@dataclass
class UploadedMaterial:
    id: int
    content: str
    date_uploaded: datetime
    user_id: int

@dataclass
class FlashCard:
    id: int
    uploaded_material_id: int
    user_id: int
    generation_date: datetime
    is_private: bool
    question: str
    answer: str
    generation_model: str

@dataclass
class Tag:
    id: int
    name: str

@dataclass
class LoginSession:
    id: int
    logged_in_date: datetime
    auth_token: str
    user_id: int