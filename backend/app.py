from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.file_uploader import FileUploader
from modules.generate_flashcard import FlashCardGenerator
from modules.flashcard_viewer import FlashCardViewer
from modules.YouTubeTrancsribe import YoutubeTranscribe
import uuid
import os

app = Flask(__name__)

CORS(app)

#This is the folder where pdf will be downloaded to 
dirName = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(dirName, 'modules', 'data', 'upload-data')
yt_rawdata_path = os.path.join(dirName, 'modules', 'data', 'youtuberaw-data')
yt_parseddata_path = os.path.join(dirName, 'modules', 'data', 'youtubeparsed-data')
flashcard_data_path = os.path.join(dirName, 'modules', 'data', 'flashcard-data')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
file_uploader = FileUploader(app)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    result = file_uploader.upload(file)
    return jsonify(result)

@app.route('/sendyoutubeurl', methods=['POST'])
def send_youtube_url():
    youtube_url = request.args.get('url')
    unique_id = str(uuid.uuid4())
    Skip_image = request.args.get('Skip_Image') #Missing flag
    youtube_parser = YoutubeTranscribe(yt_rawdata_path=yt_rawdata_path, yt_parseddata_path=yt_parseddata_path, file=unique_id, Url=youtube_url, Flag=Skip_image)
    youtube_parser.Download()
    youtube_parser.Read_Captions()
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