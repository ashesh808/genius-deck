import os
import uuid
from datetime import datetime
from sqlalchemy.orm import Session

from modules.parsers.pdf_parser import PdfParser
from modules.entities import UploadedMaterial
from modules.repositories.SqlAlchemyUserUploadedMaterials import SqlAlchemyUploadedMaterialRepository

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'pptx'}

class FileUploader:
    def __init__(self, app, session: Session):
        self.app = app
        self.Session = session

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def generate_unique_id(self):
        return str(uuid.uuid4())

    def upload(self, file, user_id):
        if file and self.allowed_file(file.filename):
            id = self.generate_unique_id()
            if file.filename.endswith('.pdf'):
                filename = id + ".pdf"
            if file.filename.endswith(".pptx"):
                filename = id + '.pptx'
            if file.filename.endswith('.txt'):
                filename = id + '.txt'
            upload_folder = self.app.config.get('UPLOAD_FOLDER')
            if not upload_folder:
                return {'error': 'UPLOAD_FOLDER configuration missing in app config'}
            upload_path = os.path.join(upload_folder, filename)
            try:
                file.save(upload_path)
                content = self.parse_file(upload_folder, filename)
                print(content)
                uploaded_material = UploadedMaterial(
                    id= 1,
                    content=content,
                    date_uploaded=datetime.now(),
                    user_id=user_id
                )
                session = self.Session
                repository = SqlAlchemyUploadedMaterialRepository(session)
                repository.add(uploaded_material)
                session.commit()
                return {'id': uploaded_material.id}
            except Exception as e:
                return {'error': f'Failed to save file: {str(e)}'}
        else:
            return {'error': 'Invalid file format'}

    def parse_file(self, file_path, filename):
        if filename.endswith('.pdf'):
            pdf_parser = PdfParser(file_path, filename)
            return pdf_parser.pdf_to_text()
        else:
            # Handle other file formats if needed
            return ''