from dataclasses import dataclass

@dataclass
class Login_Session:
    id: int
    logged_in_time: str
    auth_token: str
    user_id: int