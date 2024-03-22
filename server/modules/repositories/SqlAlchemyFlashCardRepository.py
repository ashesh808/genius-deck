from typing import List
from sqlalchemy.orm import Session
from modules.repositories.IRepository import IRepository
from modules.entities import FlashCard
from modules.models import FlashCardModel
from modules.datamappers.FlashCardDataMapper import FlashCardDataMapper

class SqlAlchemyFlashCardRepository(IRepository):
    """SqlAlchemy implementation of FlashCardRepository"""

    def __init__(self, session: Session):
        self.session = session
        self.data_mapper = FlashCardDataMapper()

    def add(self, entity: FlashCard):
        instance = self.data_mapper.entity_to_model(entity)
        self.session.add(instance)
        return instance.id

    def delete(self, entity: FlashCard):
        """Removes an existing entity from the repository."""
        model = self.session.query(FlashCardModel).get(entity.id)
        if model:
            self.session.delete(model)
            self.session.commit()

    def get(self, id) -> FlashCard:
        """Gets an entity by its ID."""
        model = self.session.query(FlashCardModel).filter_by(id=id).first()
        if model:
            return self.data_mapper.model_to_entity(model)
        return None
    
    def getAll(self) -> List[FlashCard]:
        """Gets all entities """
        flashcard_models = self.session.query(FlashCardModel).all()
        return [self.data_mapper.model_to_entity(model) for model in flashcard_models]

    def update(self, entity: FlashCard): 
        """Updates an existing entity."""
        model = self.session.query(FlashCardModel).get(entity.id)
        if model:
            self.data_mapper.update_model_with_entity(model, entity)
            self.session.commit()

    def get_by_uploaded_material_id(self, uploaded_material_id: int) -> List[FlashCard]:
        """Retrieve flashcards by uploaded_material_id"""
        flashcards = self.session.query(FlashCardModel).filter_by(uploaded_material_id=uploaded_material_id).all()
        return [self.data_mapper.model_to_entity(flashcard) for flashcard in flashcards]
    
    def commit(self):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e  