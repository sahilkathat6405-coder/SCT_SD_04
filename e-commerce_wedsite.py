import requests
from bs4 import BeautifulSoup
import csv

# Example URL (replace with an actual URL that allows scraping)
url = 'https://books.toscrape.com/'  # A great site to practice web scraping

# Send request to website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Open CSV file to write
with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Rating'])  # CSV header

    # Loop through each product on the page
    for product in soup.find_all('article', class_='product_pod'):
        # Get name
        name = product.h3.a['title']

        # Get price
        price = product.find('p', class_='price_color').text

        # Get rating from class (e.g., "star-rating Three")
        rating = product.p['class'][1]  # The second class is the rating word

        # Write to CSV
        writer.writerow([name, price, rating])

print("✅ Product data saved to 'products.csv'")
