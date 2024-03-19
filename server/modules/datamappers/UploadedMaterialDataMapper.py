from modules.datamappers.IDataMapper import IDataMapper
from modules.entities import UploadedMaterial
from modules.models import UploadedMaterialModel

class UploadedMaterialDataMapper(IDataMapper):
    def model_to_entity(self, instance: UploadedMaterialModel) -> UploadedMaterial:
        return UploadedMaterial(
            id=instance.id,
            content=instance.content,
            date_uploaded=instance.date_uploaded,
            user_id=instance.user_id
        )

    def entity_to_model(self, entity: UploadedMaterial, existing=None) -> UploadedMaterialModel:
        if existing:
            existing.content = entity.content
            existing.date_uploaded = entity.date_uploaded
            existing.user_id = entity.user_id
            return existing
        else:
            return UploadedMaterialModel(
                content=entity.content,
                date_uploaded=entity.date_uploaded,
                user_id=entity.user_id
            )