import requests 
from bs4 import BeautifulSoup 
import os

class Wiki:
    def __init__(self, url, wiki_path, file_name):
        self.url = url
        self.wiki_path = os.path.join(wiki_path, file_name + '.txt')

    def parsing(self):
    # Making a GET request 
        r = requests.get(self.url) 
        
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'lxml') 
        
        s = soup.find('div', id='bodyContent') 
        
        lines = s.find_all('p') 
        
        f = open(self.wiki_path, 'ab')
        for line in lines: 
            txt = line.text
            x = txt.encode()
            f.write(x)
            #print(line.text)

        f.close()