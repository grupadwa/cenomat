import sqlite3
import time

from bs4 import BeautifulSoup
from django.contrib import admin
from selenium import webdriver

from .models import Product


class ScrapeAction(admin.ModelAdmin):
    # Funkcja obsługująca akcję "Scrape"
    def scrape_selected_items(self, request, queryset):
        # Inicjalizacja przeglądarki (w tym przypadku Chrome)
        driver = webdriver.Chrome()

        # Połączenie z bazą danych SQLite (lub utworzenie nowej, jeśli nie istnieje)
        conn = sqlite3.connect('scraped_data.db')
        c = conn.cursor()

        # Utworzenie nowej tabeli
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

        for product in queryset:
            scrape_data(product.store_link)

        # Zatwierdzenie zmian w bazie danych
        conn.commit()

        # Zamknięcie połączenia z bazą danych
        conn.close()

        # Zamknięcie przeglądarki
        driver.quit()

    scrape_selected_items.short_description = 'Scrape selected items'

    # Dodanie przycisku "Scrape" do listy akcji dla modelu Product
    actions = ['scrape_selected_items']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'store', 'store_link', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    actions = [ScrapeAction.scrape_selected_items]  # Dodanie akcji "Scrape" do listy akcji dla modelu Product

admin.site.register(Product, ProductAdmin)
