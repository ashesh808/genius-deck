from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class GPTClientWrapper:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    def get_flashcards_with_tags(self, prompt):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You an intelligent teacher's assistant, who when given a block of text generates flash cards for it. You answer in one line your questions are marked with <question> tag and answers are marked with <answer> tag. For example: <question> What is the capital of France? <answer> Paris <question> Who is the president of the USA? <answer> Joe Biden. You must always return 3 flashcards for each prompt. You must always respond in this format."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content