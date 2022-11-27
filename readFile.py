#!/usr/bin/python
from bs4 import BeautifulSoup

with open('29-home-8.xml', encoding='utf-8') as f:
    file = f.read()

soup = BeautifulSoup(file, 'xml')
print(soup)

segments = soup.find_all('segment')

for i in range(len(segments)):
    segment = segments[i]
    print(segment)
    
    #print(unit)

# JEff is cool