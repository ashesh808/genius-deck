from sqlalchemy.orm import Session
from modules.repositories.IRepository import IRepository
from modules.entities import UploadedMaterial
from modules.models import UploadedMaterialModel
from modules.datamappers.UploadedMaterialDataMapper import UploadedMaterialDataMapper

class SqlAlchemyUploadedMaterialRepository(IRepository):
    def __init__(self, session: Session):
        self.session = session
        self.data_mapper = UploadedMaterialDataMapper()

    def add(self, entity: UploadedMaterial):
        model = self.data_mapper.entity_to_model(entity)
        self.session.add(model)

    def get(self, id: int) -> UploadedMaterial:
        model = self.session.query(UploadedMaterialModel).filter_by(id=id).first()
        if model:
            return self.data_mapper.model_to_entity(model)
        return None

    def update(self, entity: UploadedMaterial):
        model = self.session.query(UploadedMaterialModel).filter_by(id=entity.id).first()
        if model:
            updated_model = self.data_mapper.entity_to_model(entity, existing=model)
            self.session.merge(updated_model)

    def delete(self, entity: UploadedMaterial):
        model = self.session.query(UploadedMaterialModel).filter_by(id=entity.id).first()
        if model:
            self.session.delete(model)