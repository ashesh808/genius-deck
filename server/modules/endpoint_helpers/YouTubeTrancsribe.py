import os
from yt_dlp import YoutubeDL
import webvtt
import whisper
from datetime import datetime
from modules.repositories.SqlAlchemyUserUploadedMaterials import SqlAlchemyUploadedMaterialRepository
from modules.entities import UploadedMaterial

class YoutubeTranscribe:
    def __init__(self, raw_data_path, save_data_path, file_name, url, session, flag=False):
        self.file_name = file_name
        self.url = url
        self.raw_data_path = raw_data_path
        self.path = {'home' : raw_data_path}
        self.save_data_path = save_data_path
        self.audio_ext = f"{file_name}.wav"
        self.read_audio = os.path.join(raw_data_path, self.audio_ext)
        self.caption_ext = f"{file_name}.en.vtt"
        self.read_caption = os.path.join(raw_data_path, self.caption_ext)
        self.upload_repository = SqlAlchemyUploadedMaterialRepository(session)
        self.flag = flag
        self.text = ""

    def download(self, caption_test=True):
        output = {'default': self.file_name}
        ydl_opts = {
            'format': 'wav/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            'writesubtitles': True,
            'writeautomaticsub': False,
            'forcefilename': True,
            'skip_download': caption_test,
            'paths' : self.path,
            'outtmpl': output
        }

        with YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([self.url])
            except Exception as e:
                print(f"Error downloading video: {e}")

    def read_caption_data(self):
        try:
            caption_text = ''
            for caption in webvtt.read(self.read_caption):
                caption_text += caption.text + ' '
            self.text = caption_text
        except Exception as e:
            print(f"Error reading caption data: {e}")

    def transcribe_audio(self):
        
        try:
            model = whisper.load_model("base.en")

            result = model.transcribe(self.read_audio)
            text = result["text"].capitalize() + '.\n'
            self.text = text
        except Exception as e:
            print(f"Error transcribing audio: {e}")

    def write_to_database(self, user_id):
        try:
            uploaded_material = UploadedMaterial(
                id=0,
                content=self.text,
                date_uploaded=datetime.now(),
                user_id=user_id
            )
            id = self.upload_repository.add(uploaded_material)
            return id
        except Exception as e:
            print(f"Error writing to database: {e}")

    def process(self, user_id):
        if os.path.exists(self.read_caption):
            self.read_caption_data()
        else:
            print("No caption file found. Transcribing audio...")
            self.download(caption_test=True) #self.flag
            self.transcribe_audio()

        if self.text:
            id = self.write_to_database(user_id)
            return id
        else:
            print("No text available for writing to database.")