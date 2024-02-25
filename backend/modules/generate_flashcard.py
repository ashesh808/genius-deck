from modules.pdf_parser import PdfParser
from modules.gpt_client_wrapper import GPTClientWrapper
import uuid
import json
import os

class FlashCardGenerator:
    def __init__(self, pdf_path, yt_path, flashcard_path, id):
        self.id = id
        self.pdf_path = pdf_path
        self.yt_path = yt_path
        self.flashcard_path = flashcard_path
        self.parsed_data = None

    def ReadData(self, dataformat):
        if (dataformat == "pdf"):
            pdf_parser = PdfParser(self.pdf_path, file_name=self.id)
            parsed_data = pdf_parser.pdf_to_text()
            self.parsed_data = parsed_data
        elif(dataformat == "yt"):
            txt_file_path = os.path.join(self.yt_path, self.id + ".txt")
            if os.path.exists(txt_file_path):
                with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
                    parsed_data = txt_file.read()
                self.parsed_data = parsed_data
            else:
                print("Error finding the txt file")
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
        with open(filepath, 'w') as json_file:
            json.dump(jsonResponse, json_file, indent=2)
        return filename
    
    def parse_string_to_json(self,input_string):
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
            #Get response from GPT client
            gptResponse = gpt_wrapper.get_flashcards_with_tags(substring)
            print(gptResponse)
            #Convert string response to json
            jsonResponse = self.parse_string_to_json(gptResponse)
            all_responses.append(jsonResponse)
        #Save the file as Json
        name = self.save_json_response_withprefix(all_responses)
        return "Last Json file saved with name " + name
    
if __name__ == "__main__":
    id = 'FS260-Paper-1'
    dataformat = 'pdf'
    flashcard_generator = FlashCardGenerator(id)
    flashcard_generator.ReadData(dataformat)
    flashcard_generator.batch_strings()
    response = flashcard_generator.send_query()
    print(response)

    # input_string = "<questions> What is the capital of France? <answer> Paris<questions> Who is the president of the USA? <answer> Joe Biden"
    # parsed_data = flashcard_generator.parse_string_to_json(input_string)
    # print(parsed_data)


