from modules.models import FlashCardModel
from modules.entities import FlashCard
from modules.datamappers.IDataMapper import IDataMapper

class FlashCardDataMapper(IDataMapper):
    def model_to_entity(self, instance: FlashCardModel) -> FlashCard:
        return FlashCard(
            id=instance.id,
            uploaded_material_id=instance.uploaded_material_id,
            user_id=instance.user_id,
            generation_date=instance.generation_date,
            is_private=instance.is_private,
            question=instance.question,
            answer=instance.answer,
            generation_model=instance.generation_model
        )

    def entity_to_model(self, entity: FlashCard, existing=None) -> FlashCardModel:
        if existing:
            # Update the existing model instance
            existing.uploaded_material_id = entity.uploaded_material_id
            existing.user_id = entity.user_id
            existing.generation_date = entity.generation_date
            existing.is_private = entity.is_private
            existing.question = entity.question
            existing.answer = entity.answer
            existing.generation_model = entity.generation_model
            return existing
        else:
            # Create a new model instance
            return FlashCardModel(
                uploaded_material_id=entity.uploaded_material_id,
                user_id=entity.user_id,
                generation_date=entity.generation_date,
                is_private=entity.is_private,
                question=entity.question,
                answer=entity.answer,
                generation_model=entity.generation_model
            )