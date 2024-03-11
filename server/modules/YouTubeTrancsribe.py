import os
from yt_dlp import YoutubeDL
import webvtt
import time
import whisper


class YoutubeTranscribe:
    #initilizes the class with variables i need
    def __init__ (self, raw_data_path, Save_data_path, File_Name, URL, Flag=bool):
        self.file = str(File_Name)
        self.Url = URL
        self.path = {'home' : raw_data_path}
        self.Read_Raw = raw_data_path
        self.Audext = self.file + '.wav'
        self.ReadAud = os.path.join(raw_data_path, self.Audext)
        self.SaveAud = Save_data_path
        self.ext = self.file + '.en.vtt'
        self.Read = os.path.join(raw_data_path, self.ext)
        self.Save = Save_data_path
        self.Flag = Flag
    # downloads the data from youtube
    def Download(self, Caption_Test=True):
        output = {'default' : self.file}
        #making a dictionary of the options i want to include with the download
        ydl_opts = {
            'format' : 'wav/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'wav',
            }],
            'writesubtitles' : True,
            'writeautomaticsub' : False,
            'forcefilename' : True,
            'skip_download' : Caption_Test,
            'paths' : self.path,
            'outtmpl' : output
        }

        URL = [self.Url]
        with YoutubeDL(ydl_opts) as ydl :
            ydl.download(URL)
    #tries to read the captions from the youtube video
    def TryCaptionData(self):
        time.sleep(1)
        cap =''
        for caption in webvtt.read(self.Read):
            cap = cap + caption.text + ' '
        savename = self.file + '.txt'
        location = os.path.join(self.Save, savename)
        cap.strip('\n')
        try:
            os.remove(location)
        except:
            pass
        f = open(location, 'a')
        f.write(cap)
        f.close
        os.remove(self.Read)
    #sends audio to googles speech recognition API

    def LargeAudioParse(self):
        WholeText = ''
        model = whisper.load_model('base.en')
        try:        
            result = model.transcribe(self.ReadAud)
            text = result['text']
        except:
            pass
            #print("Error", str(e))
        else:
            text = f'{text.capitalize()}.\n'
            #print(chunk_filename, ':', text)
            WholeText += text
        self.text = WholeText
        #return(WholeText)

    def WriteToFile(self):
        file = self.file + '.txt'
        path = os.path.join(self.SaveAud, file)
        f = open(path, 'a')
        f.write(self.text)
        f.close()
        #shutil.rmtree(os.path.join(self.Read_Raw, 'AudioChunks'))
        os.remove(self.ReadAud)

    def Read_Captions(self):
        if os.path.exists(self.Read) == True:
            self.TryCaptionData()
        elif self.Flag != 'True':
            print("Reading caption data failed.")
            print('Parsing audio this may take a while.')
            self.Download(False)
            self.LargeAudioParse()
            self.WriteToFile()

if __name__ =="__main__":
    rawdata = input()
    savedate = input()
    Filename = input()
    UrL = input()
    start_time = time.time()
    Test = YoutubeTranscribe(rawdata, savedate, Filename, UrL, False)
    Test.Download()
    Test.Read_Captions()
    print("--- %s seconds ---" % (time.time() - start_time))