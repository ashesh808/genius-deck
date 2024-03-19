import os
import uuid
from datetime import datetime
from sqlalchemy.orm import Session

from modules.parsers.pdf_parser import PdfParser
from modules.parsers.pptx_parser import PptxParser
from modules.entities import UploadedMaterial
from modules.repositories.SqlAlchemyUserUploadedMaterials import SqlAlchemyUploadedMaterialRepository

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'pptx'}

class FileUploader:
    def __init__(self, app, session: Session):
        self.app = app
        self.Session = session

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def upload(self, file, user_id):
        if file and self.allowed_file(file.filename):
            id = "placeholder"
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
                uploaded_material = UploadedMaterial(
                    id=0, 
                    content=content,
                    date_uploaded=datetime.now(),
                    user_id=user_id
                )
                session = self.Session
                repository = SqlAlchemyUploadedMaterialRepository(session)
                id = repository.add(uploaded_material)
                return {'id': id}
            except Exception as e:
                return {'error': f'Failed to save file: {str(e)}'}
        else:
            return {'error': 'Invalid file format'}

    def parse_file(self, file_path, filename):
        path = os.path.join(file_path, filename)
        if filename.endswith('.txt'):
            data = open(path, 'r')
            return data.read()
        if filename.endswith('.pdf'):
            pdf_parser = PdfParser(path)
            return pdf_parser.parse()
        if filename.endswith('.pptx'):
            pptx_parser = PptxParser(path)
            return pptx_parser.parse()
        else:
            # Handle other file formats if needed
            return ''
