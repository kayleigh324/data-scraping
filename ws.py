import requests
from bs4 import BeautifulSoup

url = 'https://www.wsj.com/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <span> elements with the specified class
span_article_titles = soup.find_all('span', class_='WSJTheme--headlineText--He1ANr9C')

# Find all the <h3> elements with the specified class
h3_article_titles = soup.find_all('h3', class_='WSJTheme--headline--unZqjb45 reset WSJTheme--heading-15--3sylkGaL typography--serif-display--ZXeuhS5E')

# Find all the <h3> elements within <article> tags
article_titles = [article.find('h3') for article in soup.find_all('article', class_='WSJTheme--story--XB4V2mLz WSJTheme--story-padding--1gRL3tuf WSJTheme--border-bottom--s4hYCt0s')]

# Extract and print the text from the <span> elements
for title in span_article_titles:
    print(title.text)

# Extract and print the text from the <h3> elements
for title in h3_article_titles:
    print(title.text)

# Extract and print the text from the <h3> elements within <article> tags
for title in article_titles:
    print(title.text)
