import requests 
from bs4 import BeautifulSoup 
from datetime import datetime

from modules.repositories.SqlAlchemyUserUploadedMaterials import SqlAlchemyUploadedMaterialRepository
from modules.entities import UploadedMaterial

class Wiki:
    def __init__(self, url, session):
        self.url = url
        self.upload_repository = SqlAlchemyUploadedMaterialRepository(session)

    def parse(self, user_id):
        try:
            r = requests.get(self.url)
            soup = BeautifulSoup(r.content, 'lxml')
            body_content = soup.find('div', id='bodyContent')
            paragraphs = body_content.find_all('p')
            text = '\n'.join([p.text for p in paragraphs])
            return self.write_to_database(text, user_id)
        except Exception as e:
            print(f"Error parsing webpage: {e}")

    def write_to_database(self, content, user_id):
        try:
            scraped_material = UploadedMaterial(
                id=0,
                content=content,
                date_uploaded=datetime.now(),
                user_id= user_id
            )
            id = self.upload_repository.add(scraped_material)
            return id
        except Exception as e:
            print(f"Error writing to database: {e}")