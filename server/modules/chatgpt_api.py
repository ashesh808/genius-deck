import openai

class ChatGPT_API:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key
        
    def get_completion(self, prompt):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = messages,
            temperature = 0,
        )
        return response.choices[0].message["content"]
