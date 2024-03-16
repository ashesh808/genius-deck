from dataclasses import dataclass

@dataclass
class User:
    id: int
    user_name: str
    password: str
    user_email: str
    first_name: str
    last_name: str
    reg_time: str