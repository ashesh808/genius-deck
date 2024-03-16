from dataclasses import dataclass

@dataclass
class Flash_Cards:
    id: int
    uploaded_material_id: int
    user_id: int
    gen_date: str
    is_private: bool
    question: str
    answer: str
    model: str