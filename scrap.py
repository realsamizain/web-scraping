from requests import get
url = 'http://www.tarabyon.com/en/music.asp?letter=a'
response = get(url)
from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
artist = html_soup.find_all('div', class_ = 'padder-v')
print(len(artist))
first_artist = artist[0]
print(first_artist)
print(first_artist.a)
print(first_artist.a.text)
for x in artist:
 print(x.a.text)
