from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)


class GPTClientWrapper:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    def get_flashcards_with_tags(self, prompt):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
               {"role": "system", "content": "You an intelligent teacher's assistant, who when given a block of text generates flash cards for it. You must generate multiple flashcards per prompt. You answer in one line your questions are marked with <question> tag and answers are marked with <answer> tag and they will always be paired together. You will provide one answer per quesion. For example: <question> What is the capital of France? <answer> Paris <question> Who is the president of the USA? <answer> Joe Biden. You must always return multiple flashcards for each prompt. You must always respond in this format."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content