from flask import Flask, jsonify
import os
import uuid

ALLOWED_EXTENSIONS = {'pdf'}

class PDFUploader:
    
    def __init__(self, app):
        self.app = app

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def upload_pdf(self, file):
        if file and self.allowed_file(file.filename):
            # Generate a unique ID for the file
            unique_id = str(uuid.uuid4())
            # Ensure the folder exists
            os.makedirs(self.app.config['UPLOAD_FOLDER'], exist_ok=True)
            # Save the file with the unique ID as the filename
            file.save(os.path.join(self.app.config['UPLOAD_FOLDER'], f"{unique_id}.pdf"))
            return {'id': unique_id}
        else:
            return {'error': 'Invalid file format'}