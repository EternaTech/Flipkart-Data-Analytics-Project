import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

Product_name = []
prices = []
ratings = []
descriptions = []

for page in range(1, 300):
    url = f"https://www.flipkart.com/search?q=smart%20phone&page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    cards = soup.find_all("a", class_="k7wcnx")
    print(f"Found {len(cards)} product cards on page {page}.\n")

    for c in cards:
        title_tag = c.find("div", class_="RG5Slk")
        title = title_tag.text.strip() if title_tag else "N/A"
        Product_name.append(title)

        price_tag = c.find("div", class_="hZ3P6w")
        price = price_tag.text.strip() if price_tag else "N/A"
        prices.append(price)

        rating_tag = c.find("div", class_="MKiFS6")
        rating = rating_tag.text.strip() if rating_tag else "N/A"
        ratings.append(rating)

        specs_list = []
        specs_ul = c.find("ul", class_="HwRTzP")
        if specs_ul:
            for li in specs_ul.find_all("li", class_="DTBslk"):
                specs_list.append(li.text.strip())

        desc = " | ".join(specs_list) if specs_list else "N/A"
        descriptions.append(desc)

    print("Waiting 1 seconds before next page...\n")
    time.sleep(1)

    data = pd.DataFrame({
        "Product Name": Product_name,
        "Price": prices,
        "Rating": ratings,
        "Description": descriptions
    })
    data.to_csv("flipkart_smartphones.csv", index=False)
