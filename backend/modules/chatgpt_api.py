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

if __name__ == "__main__":
    api_key = ''

    chatbot = ChatGPT_API(api_key)

    prompt = "Who won the Grammy for best rock album in 2020?"

    response = chatbot.get_completion(prompt)

    print(response)