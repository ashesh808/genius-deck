from modules.parsers.new_pdf import PdfParse
from modules.generators.gpt_client_wrapper import GPTClientWrapper
from modules.parsers.powerpoint import Powerpoint
import uuid
import json
import os
import io

class FlashCardGenerator:
    def __init__(self, Upload_Path, yt_path, wiki_path, flashcard_path, id, Skip_Image):
        self.id = id
        self.Upload_Path = Upload_Path
        self.yt_path = yt_path
        self.flashcard_path = flashcard_path
        self.parsed_data = None
        self.Skip_Image = Skip_Image
        self.wiki_path = wiki_path

    def ReadData(self, dataformat):
        if (dataformat == "pdf"):
            pdf_parser = PdfParse(self.Upload_Path, file_name=self.id, Skip_image=self.Skip_Image)
            parsed_data = pdf_parser.ReadPdf()
            self.parsed_data = parsed_data
        elif(dataformat == "yt"):
            txt_file_path = os.path.join(self.yt_path, self.id + ".txt")
            if os.path.exists(txt_file_path):
                with open(txt_file_path, 'r') as txt_file:
                    parsed_data = txt_file.read()
                self.parsed_data = parsed_data
            else:
                print("Error finding the txt file")
        elif(dataformat == "pptx"):
            pptx = Powerpoint(self.Upload_Path, self.id, self.Skip_Image)
            parsed_data = pptx.PptToText()
            self.parsed_data = parsed_data
        elif(dataformat == "wiki"):
            path = os.path.join(self.wiki_path, self.id + '.txt')
            data = open(path, 'r')
            self.parsed_data = data.read()
        elif(dataformat == 'txt'):
            path = os.path.join(self.Upload_Path, self.id + '.txt')
            data = open(path, 'r', encoding='UTF-8')
            self.parsed_data = data.read()
        else:
            raise NotImplementedError("Data format not supported yet")

    def batch_strings(self):
        if self.parsed_data is not None:
            max_length = 4000
            substrings = [self.parsed_data[i:i + max_length] for i in range(0, len(self.parsed_data), max_length)]
            return substrings
        else:
            raise ValueError("No data available. Call ReadData first to parse data.")
    
    def save_json_response_withprefix(self, jsonResponse):
        filename = self.id + ".json"
        filepath = os.path.join(self.flashcard_path, filename)
        with open(filepath, 'a') as json_file:
            json.dump(jsonResponse, json_file, indent=2)
        return filename
    
    def parse_string_to_json(self, input_string):
        data_list = []
        sets = input_string.split("<question>")
        for set_part in sets[1:]:
            set_parts = set_part.split("<answer>")
            if len(set_parts) == 2:
                question, answer = set_parts
                question = question.strip()
                answer = answer.strip()
            data_list.append({"question": question, "answer": answer})
        return data_list


    def send_query(self):
        gpt_wrapper = GPTClientWrapper()
        substrings = self.batch_strings()
        all_responses = []
        name = ":not executed"
        for i, substring in enumerate(substrings):
            gptResponse = gpt_wrapper.get_flashcards_with_tags(substring)
            print(gptResponse)
            jsonResponse = self.parse_string_to_json(gptResponse)
            all_responses.append(jsonResponse)
        name = self.save_json_response_withprefix(all_responses)
        return "Last Json file saved with name " + name
