from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
  global pages
  html = urlopen(f'hrml://en.wikipedia.org{pageUrl}')
  bs = BeautifulSoup(html,'html.parser')

  try:
    print(bs.h1.get_tex())
    print(bs.find(id='mw-content-text').find_all('p')[0])
    print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
  except AttributeError: 
    print('This page is missing something! Continuing.')

  for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
    if 'href' in link.attrs:
      if link.attrs['href'] not in pages:
        newPage = link.attrs['href']
        print('-'*20)
        print(newPage)
        pages.add(newPage)

        while len(pages) < 3:
          getLinks(newPage)

getLinks('')