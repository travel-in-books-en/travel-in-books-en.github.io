import bs4, requests

response = requests.get('https://travel-in-books-en.github.io/',headers={'User-Agent': 'Mozilla/5.0'})
print(response.text)
# soup = bs4.BeautifulSoup(response.text)
# soup.body.get_text(' ', strip=True)
