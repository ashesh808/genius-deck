from models import FlashCardModel
from entities import FlashCards
from datamappers.IDataMapper import IDataMapper

class FlashCardDataMapper(IDataMapper):
    def model_to_entity(self, instance: FlashCardModel) -> FlashCards:
        return FlashCards(
            id=instance.id,
            uploaded_material_id=instance.uploaded_material_id,
            user_id=instance.user_id,
            gen_date=instance.gen_date,
            is_private=instance.is_private,
            question=instance.question,
            answer=instance.answer,
            model=instance.model
        )

    def entity_to_model(self, entity: FlashCards, existing=None) -> FlashCardModel:
        if existing:
            # Update the existing model instance
            existing.uploaded_material_id = entity.uploaded_material_id
            existing.user_id = entity.user_id
            existing.gen_date = entity.gen_date
            existing.is_private = entity.is_private
            existing.question = entity.question
            existing.answer = entity.answer
            existing.model = entity.model
            return existing
        else:
            # Create a new model instance
            return FlashCardModel(
                uploaded_material_id=entity.uploaded_material_id,
                user_id=entity.user_id,
                gen_date=entity.gen_date,
                is_private=entity.is_private,
                question=entity.question,
                answer=entity.answer,
                model=entity.model
            )