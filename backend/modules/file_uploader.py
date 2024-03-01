import os
import uuid
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'pptx'}

class FileUploader:
    def __init__(self, app):
        self.app = app

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def generate_unique_id(self):
        return str(uuid.uuid4())

    def upload(self, file):
        if file and self.allowed_file(file.filename):
            #NOTE: Temporary fix, need to change after complete support for other file formats
            id = self.generate_unique_id()
            filename = id + ".pdf"
            upload_folder = self.app.config.get('UPLOAD_FOLDER')
            if not upload_folder:
                return {'error': 'UPLOAD_FOLDER configuration missing in app config'}
            upload_path = os.path.join(upload_folder, filename)
            try:
                file.save(upload_path)
                return {'id': id}
            except Exception as e:
                return {'error': f'Failed to save file: {str(e)}'}
        else:
            return {'error': 'Invalid file format'}
