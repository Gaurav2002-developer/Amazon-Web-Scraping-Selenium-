from bs4 import BeautifulSoup
import pandas as pd
import os

data = {'title': [], 'price': [], 'link': [] , 'arrival' : []}

files = os.listdir('data')
print(f"Total files found: {len(files)}")

for file in files:
    try:
        if file.endswith('.html'):
            with open(f"data/{file}", 'r', encoding='utf-8') as f:
                html_doc = f.read()

            soup = BeautifulSoup(html_doc, "html.parser")

            # 🔹 Find the product container
            product_div = soup.find("div", class_="puisg-row")

            if product_div:
                # 🔹 Extract title and link (look for <a> with class containing 'a-link-normal s-no-hover')
                title_tag = product_div.find("a", href = True)
                title = title_tag.get_text(strip=True) if title_tag else "N/A"
                link = "https://www.amazon.in" + title_tag["href"] if title_tag and title_tag.has_attr("href") else "N/A"

                # 🔹 Extract price
                price_tag = product_div.find("span", class_="a-price-whole")
                price = price_tag.get_text(strip=True) if price_tag else "N/A"

                arrival_tag = product_div.find("div" , { 'data-cy' : "delivery-recipe"})
                arrival = arrival_tag.get_text(strip=True) if arrival_tag else "N/A"

                data['title'].append(title)
                data['price'].append(price)
                data['link'].append(link)
                data["arrival"].append(arrival)

                print(f"Title: {title}\nPrice: {price}\nLink: {link}\nArrival: {arrival}\n---")

    except Exception as e:
            print(e)

print(f"\nExtracted {len(data['title'])} products.")

df = pd.DataFrame(data)
df.to_csv('data.csv')
