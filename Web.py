from bs4 import BeautifulSoup
import requests
import pandas as pd

# Read the HTML content (assuming Amazon.html is the HTML file)
with open('Amazon.html', 'r', encoding='utf8') as file:
    html_content = file.read()

# Parse HTML using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with specified class
product_divs = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2hrdt6w0jdtp122jn0441sgwu4 s-latency-cf-section puis-card-border')

# Lists to store product details
product_names = []
product_prices = []
product_ratings = []

# Extract information from each div
for div in product_divs:
    # Extract Product Name
    product_name_element = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_name = product_name_element.text.strip() if product_name_element else ''
    product_names.append(product_name)

    # Extract Product Price
    product_price_element = div.find('span', class_='a-price-whole')
    product_price = product_price_element.text.strip() if product_price_element else ''
    product_prices.append(product_price)

    # Extract Product Rating
    product_rating_element = div.find('span', class_='a-size-base s-underline-text')
    product_rating = product_rating_element.text.strip() if product_rating_element else ''
    product_ratings.append(product_rating)

# Create a DataFrame with the extracted data
data = {
    'Product_Name': product_names,
    'Product_Price': product_prices,
    'Product_Rating': product_ratings
}
df = pd.DataFrame(data)

# Write to Excel file
df.to_excel('Amazon_Products.xlsx', index=False)