import json
from sqlalchemy.orm import Session
from modules.repositories.SqlAlchemyFlashCardRepository import SqlAlchemyFlashCardRepository

class FlashCardViewer:
    def __init__(self, session: Session):
        self.flashcard_repository = SqlAlchemyFlashCardRepository(session)

    def ViewAllFlashCards(self):
        flashcards = self.flashcard_repository.getAll()
        json_data = []
        for flashcard in flashcards:
            flashcard_data = {
                "question": flashcard.question,
                "answer": flashcard.answer
            }
            json_data.append(flashcard_data)
        return json.dumps(json_data, indent=2)

        
    def ViewFlashCardByUploadID(self, uploaded_material_id):
        flashcards = self.flashcard_repository.get_by_uploaded_material_id(uploaded_material_id)
        json_data = []
        for flashcard in flashcards:
            flashcard_data = {
                "question": flashcard.question,
                "answer": flashcard.answer
            }
            json_data.append(flashcard_data)
        return json.dumps(json_data, indent=2)