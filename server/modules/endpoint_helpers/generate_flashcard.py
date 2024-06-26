import os
from sqlalchemy.orm import Session
from datetime import datetime

from modules.repositories.SqlAlchemyUserUploadedMaterials import SqlAlchemyUploadedMaterialRepository
from modules.repositories.SqlAlchemyFlashCardRepository import SqlAlchemyFlashCardRepository
from modules.entities import FlashCard
from modules.generators.gpt_client_wrapper import GPTClientWrapper

class FlashCardGenerator:
    def __init__(self, id, yt_path, wiki_path, Skip_Image, session: Session):
        self.id = id
        self.yt_path = yt_path
        self.parsed_data = None
        self.Skip_Image = Skip_Image
        self.wiki_path = wiki_path
        self.uploaded_material_repository = SqlAlchemyUploadedMaterialRepository(session)
        self.flashcard_repository = SqlAlchemyFlashCardRepository(session)
        self.uploaded_material = self.uploaded_material_repository.get(self.id)

    def ReadData(self, dataformat):
            self.parsed_data = self.uploaded_material.content
            print(self.parsed_data)

    def batch_strings(self):
        if self.parsed_data is not None:
            max_length = 8000
            substrings = [self.parsed_data[i:i + max_length] for i in range(0, len(self.parsed_data), max_length)]
            return substrings
        else:
            raise ValueError("No data available. Call ReadData first to parse data.")
    
    def save_flashcards_to_db(self, flashcards):
        flashcard_ids = []
        for flashcard in flashcards:
            flashcard_id = self.flashcard_repository.add(flashcard)
            flashcard_ids.append(flashcard_id)
        self.flashcard_repository.commit()
        print("Flashcards commited to db")
        return flashcard_ids
    
    def parse_string_to_flashcards(self, input_string):
        flashcards = []
        sets = input_string.split("<question>")
        for set_part in sets[1:]:
            set_parts = set_part.split("<answer>")
            if len(set_parts) == 2:
                question, answer = set_parts
                question = question.strip()
                answer = answer.strip()
                flashcard = FlashCard(
                    id=None,  # Assuming id will be assigned by the database
                    uploaded_material_id=self.uploaded_material.id,
                    user_id=self.uploaded_material.user_id,
                    generation_date=datetime.now(),
                    is_private=False,  # You can set this value based on your logic
                    question=question,
                    answer=answer,
                    generation_model="gpt-3.5 turbo"  # You can set this value based on your logic
                )
                flashcards.append(flashcard)
        return flashcards
    
    def check_response_format(self, response):
        parts = response.split("<question>")
        # Check if there are at least two parts (question and answer)
        if len(parts) < 2:
            return False
        for part in parts[1:]:
            if "<answer>" not in part:
                return False
        return True
    
    def send_query(self, max_retries=5):
        gpt_wrapper = GPTClientWrapper()
        substrings = self.batch_strings()
        all_responses = []
        for substring in substrings:
            retries = 0
            while retries < max_retries:
                gptResponse = gpt_wrapper.get_flashcards_with_tags(substring)
                print("Received response:", gptResponse)
                if self.check_response_format(gptResponse):
                    flashcards = self.parse_string_to_flashcards(gptResponse)
                    all_responses.extend(flashcards)
                    break
                else:
                    retries += 1
                    print("Response format incorrect. Retrying... Attempt:", retries)
                    if retries >= max_retries:
                        print("Maximum retries reached for this substring.")
                        break
        self.save_flashcards_to_db(all_responses)

