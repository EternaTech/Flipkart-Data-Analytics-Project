from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

product_name, price, discription, rating, page_number = [], [], [], [], []

# Function to extract text from a card element
def get_text(card, tag, class_name):
    item = card.find(tag, class_ = class_name)
    return item.get_text(strip=True) if item else 'N/A'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}

# Loop through the first page till the last page of search results
for page in range(1,300):

    url = "PUT_YOUR_URL_HERE"
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    cards = soup.find_all('div', class_ = 'jIjQ8S')
    print('Page',page,"| Cards", len(cards))

# If there are no cards found, break the loop
    if not cards:
        print("No more products. Stopping.")
        break

# Loop through each card and extract the required information
    for card in cards:
        # Product Name
        product_name.append(get_text(card, 'div', 'RG5Slk'))

        # Price
        price.append(get_text(card, 'div', 'hZ3P6w DeU9vF'))

        # Discription
        discription.append(get_text(card, 'ul', 'HwRTzP'))

        # Rating
        rating.append(get_text(card, 'div', 'MKiFS6'))

        page_number.append(page)
    
    print("Page", page, "completed")
    time.sleep(1)

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'Product Name': product_name,
    'Price': price,
    'Discription': discription,
    'Rating': rating,
    'Page Number': page_number
})
print(df)

# Save data to CSV
df.to_csv("flipkart_products.csv", index=False)

print("Data saved successfully!")
