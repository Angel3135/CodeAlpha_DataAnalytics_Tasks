import requests
from bs4 import BeautifulSoup
import pandas as pd

books_data = []
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 51):  # 50 pages = 1000 books
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books_data.append([title, price])

df = pd.DataFrame(books_data, columns=['Title', 'Price'])
df.to_csv('books_dataset.csv', index=False, encoding='utf-8')
print("1000 books scraped successfully!")