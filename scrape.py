from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

product_name = []
price = []
discription = []
rating = []
page_number = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}

for page in range(1,5):

    url = "https://www.flipkart.com/search?q=phone+touch+screen"
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    cards = soup.find_all('div', class_ = 'jIjQ8S')
    print('Page',page,"| Cards", len(cards))

    for card in cards:
        # Product Name
        product_name = card.find('div', class_ = 'RG5Slk')

        # Price
        price = card.find('div', class_ = 'hZ3P6w DeU9vF')

        # Discription
        discription = card.find('ul', class_ = 'HwRTzP')

        # Rating
        rating = card.find('div', class_ = 'MKiFS6')

        product_name.append(product_name.get_text(strip=True) if product_name else 'N/A')
        price.append(price.get_text(strip=True) if price else 'N/A')
        discription.append(discription.get_text(strip=True) if discription else 'N/A')
        rating.append(rating.get_text(strip=True) if rating else 'N/A')

        page_number.append(page)
    print("Page", page, "completed")
    time.sleep(2)


df = pd.DataFrame({
    'Product Name': product_name,
    'Price': price,
    'Discription': discription,
    'Rating': rating,
    'Page Number': page_number
})
print(df)
