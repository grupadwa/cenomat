from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3

# Inicjalizacja przeglądarki (w tym przypadku Chrome)
driver = webdriver.Chrome()

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()

# Create a new table
c.execute('''
    CREATE TABLE IF NOT EXISTS products
    (store_name text, product_name text, price text, link text)
''')

def scrape_data(url):
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    product_names = soup.find_all('h4', {'class': 'box-medium__title | body-1-b'})
    product_prices = soup.find_all('div', {'class': 'price__value'})
    base_url = 'https://www.euro.com.pl/'
    results = ""
    for name, price in zip(product_names, product_prices):
        store_name = 'Euro RTV AGD'
        product_link = base_url + name.find('a')['href']
        results += f"Product Name: {name.text.strip()}, Price: {price.text.strip()}, Link: {product_link}\n"
        c.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                  (store_name, name.text.strip(), price.text.strip(), product_link))
    print(results)

# Skrapowanie danych ze wszystkich stron
urls = [
    'https://www.euro.com.pl/konsole-nintendo-switch.bhtml',
    'https://www.euro.com.pl/konsole-playstation-4.bhtml',
    'https://www.euro.com.pl/konsole-playstation-5.bhtml',
    'https://www.euro.com.pl/konsole-xbox-series.bhtml'
]

for url in urls:
    scrape_data(url)

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()

# Zamknięcie przeglądarki
driver.quit()
