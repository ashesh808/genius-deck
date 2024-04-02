from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os, time
import random


from modules.endpoint_helpers.file_uploader import FileUploader
from modules.endpoint_helpers.generate_flashcard import FlashCardGenerator
from modules.endpoint_helpers.flashcard_viewer import FlashCardViewer
from modules.endpoint_helpers.YouTubeTrancsribe import YoutubeTranscribe
from modules.endpoint_helpers.webpage import Wiki
from modules.endpoint_helpers.login_manager import LoginManager


app = Flask(__name__)
login_manager = LoginManager(app)

CORS(app)

#This is the folder where pdf will be downloaded to 
dirName = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(dirName, 'modules', 'data', 'upload-data')
wiki_parseddata_path = os.path.join(dirName, 'modules', 'data', 'wikiraw-data')
yt_rawdata_path = os.path.join(dirName, 'modules', 'data', 'youtuberaw-data')
yt_parseddata_path = os.path.join(dirName, 'modules', 'data', 'youtubeparsed-data')

# Set up the database engine and sessionmaker
engine = create_engine(os.environ.get("DB_URL"))
Session = sessionmaker(bind=engine)
session = Session()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
file_uploader = FileUploader(app, session)
flashcard_viewer = FlashCardViewer(session = session)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    user_id = 1
    result = file_uploader.upload(file, user_id)
    return jsonify(result)

@app.route('/sendyoutubeurl', methods=['POST'])
def send_youtube_url():
    youtube_url = request.args.get('url')
    Skip_Audio = request.args.get('AudSkip')
    user_id = 1
    youtube_parser = YoutubeTranscribe(raw_data_path=yt_rawdata_path, save_data_path=yt_parseddata_path, file_name="placeholder", url=youtube_url, session=session, flag=Skip_Audio)
    youtube_parser.download()
    id = youtube_parser.process(user_id)
    return jsonify({'id': id})

@app.route('/sendwikiurl', methods=['POST'])
def send_wiki_url():
    wiki_url = request.args.get('url')
    if not wiki_url:
        return jsonify({'error': 'URL parameter is missing'})
    user_id = 1
    wiki_parser = Wiki(url=wiki_url, session=session)
    id = wiki_parser.parse(user_id)
    return jsonify({'id': id})

#Change this to POST
@app.route('/generatecards', methods=['GET'])
def generate_flashcards():
    id = request.args.get('id')
    dataformat = request.args.get('dataformat')
    #Skip_Image = request.args.get('imgSkip')
    flashcard_generator = FlashCardGenerator(id=id, yt_path=yt_parseddata_path, wiki_path=wiki_parseddata_path, Skip_Image=True, session=session)
    flashcard_generator.ReadData(dataformat)
    flashcard_generator.batch_strings()
    response = flashcard_generator.send_query()
    time.sleep(5)
    print(response)
    return jsonify({'id': id})

@app.route('/getflashcarddata', methods=['GET'])
def get_flashcard_data():
    uploaded_material_id = request.args.get('id')
    if not uploaded_material_id:
        return jsonify({'error': 'id parameter is missing'})
    return flashcard_viewer.ViewFlashCardByUploadID(uploaded_material_id)

@app.route('/browse', methods=['GET'])
def get_all_flashcards():
    return flashcard_viewer.ViewAllFlashCards()

@app.route('/login', methods=['POST'])
def login():
    user_id = 1 
    login_manager.login(user_id)

@app.route('/logout', methods=['POST'])
def logout():
    login_manager.logout()

if __name__ == '__main__':
    app.run(debug=True)