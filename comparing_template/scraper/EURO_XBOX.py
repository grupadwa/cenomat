from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('euro x box.db')
c = conn.cursor()

# Create a new table
c.execute('''
    CREATE TABLE products
    (store_name text, product_name text, price text, link text)
''')
conn.commit()


url = 'https://www.euro.com.pl/konsole-xbox-series.bhtml'

# Inicjalizacja przeglądarki (w tym przypadku Chrome)
driver = webdriver.Chrome()

driver.get(url)

# Czekaj na załadowanie dynamicznej zawartości
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

product_names = soup.find_all('h4', {'class': 'box-medium__title | body-1-b'})
product_prices = soup.find_all('div', {'class': 'price__value'})
base_url = 'https://www.euro.com.pl/'

results = ""

for name, price in zip(product_names, product_prices):
    store_name = 'Euro RTV AGD'
    product_link = base_url + name.find('a')['href']  # find the 'a' tag and get the href attribute
    results += f"Product Name: {name.text.strip()}, Price: {price.text.strip()}, Link: {product_link}\n"
# Insert the scraped data into the table
    c.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
              (store_name, name.text.strip(), price.text.strip(), product_link))
print(results)

conn.commit()

driver.quit()

# Close the connection to the database
conn.close()