import os
import json

class FlashCardViewer:
    def __init__(self, ID, flashcard_path):
        self.FlashID = ID
        self.path = self.ReturnPath(flashcard_path)

    def ReturnPath(self, flashcard_path):
        self.FlashID = str(self.FlashID)
        return os.path.join(flashcard_path, f"{self.FlashID}.json")

    def ReadJson(self):
        try:
            with open(self.path, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return "File does not exist"
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

