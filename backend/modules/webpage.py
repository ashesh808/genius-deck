import requests 
from bs4 import BeautifulSoup 
  
URL = input()
# Making a GET request 
r = requests.get(URL) 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'lxml') 
  
s = soup.find('div', id='bodyContent') 
  
lines = s.find_all('p') 
  
f = open('test.txt', 'ab')
for line in lines: 
    txt = line.text
    x = txt.encode()
    f.write(x)
    #print(line.text)

f.close()