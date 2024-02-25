from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.pdf_uploader import PDFUploader
from modules.generate_flashcard import FlashCardGenerator
from modules.flashcard_viewer import FlashCardViewer
from modules.youtube_parser import YoutubeParser
import uuid
import os

app = Flask(__name__)

CORS(app)

#This is the folder where pdf will be downloaded to 
dirName = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(dirName, 'modules', 'data', 'pdfdocument')
yt_rawdata_path = os.path.join(dirName, 'modules', 'data', 'youtuberawdata')
yt_parseddata_path = os.path.join(dirName, 'modules', 'data', 'youtubeparseddata')
flashcard_data_path = os.path.join(dirName, 'modules', 'data', 'flashcarddata')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
pdf_uploader = PDFUploader(app)


@app.route('/uploadpdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    result = pdf_uploader.upload_pdf(file)
    return jsonify(result)

@app.route('/sendyoutubeurl', methods=['POST'])
def send_youtube_url():
    youtube_url = request.args.get('url')
    unique_id = str(uuid.uuid4())
    youtube_parser = YoutubeParser(yt_rawdata_path=yt_rawdata_path, yt_parseddata_path=yt_parseddata_path, file=unique_id, Url=youtube_url)
    youtube_parser.Download()
    youtube_parser.ReadCaptions()
    return jsonify({'id': unique_id})

@app.route('/generatecards', methods=['GET'])
def generate_flashcards():
    id = request.args.get('id')
    dataformat = request.args.get('dataformat')
    flashcard_generator = FlashCardGenerator(pdf_path=UPLOAD_FOLDER, yt_path=yt_parseddata_path, flashcard_path=flashcard_data_path, id=id)
    flashcard_generator.ReadData(dataformat)
    flashcard_generator.batch_strings()
    response = flashcard_generator.send_query()
    print(response)
    return jsonify({'id': id})

@app.route('/getflashcarddata', methods=['GET'])
def get_flashcard_data():
    flashcard_id = request.args.get('id')
    if not flashcard_id:
        return jsonify({'error': 'ID parameter is missing'})
    flashcard_viewer = FlashCardViewer(flashcard_path=flashcard_data_path, ID=flashcard_id)
    flashcard_data = flashcard_viewer.ReadJson()
    return flashcard_data

if __name__ == '__main__':
    app.run(debug=True)