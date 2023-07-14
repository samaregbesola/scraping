import requests
import json
import pandas as pd

shoes = []
# fetching = True

url = f"https://api.nike.com/product_feed/rollup_threads/v2?filter=marketplace%28US%29&filter=language%28en%29&filter=employeePrice%28true%29&filter=attributeIds%2816633190-45e5-4830-a068-232ac7aea82c%2C8529ff38-7de8-4f69-973c-9fdbfb102ed2%29&anchor=0&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=60"

while url:
    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    shoes += json_data["objects"]
    if json_data['pages']['next'] != '':
        url = f"https://api.nike.com{json_data['pages']['next']}"
    else:
        url = None

#process shoes
shoes

data = []
for shoe in shoes:
    id = shoe['productInfo'][0]["merchProduct"]["pid"]
    title = shoe['productInfo'][0]["productContent"]["title"]
    category = shoe['productInfo'][0]["productContent"]["subtitle"]
    price = shoe['productInfo'][0]['merchPrice']['fullPrice']
    color = shoe['productInfo'][0]["productContent"]["colors"][0]["name"]
    inStock = shoe['productInfo'][0]['availability']['available']
    img_one = shoe["publishedContent"]["nodes"][0]["nodes"][0]["properties"]["squarish"]["url"] if shoe["publishedContent"]["nodes"][0]["nodes"][0]["properties"] != {} else shoe["publishedContent"]["nodes"][0]["nodes"][4]["properties"]["squarish"]["url"]
    img_two = shoe["publishedContent"]["nodes"][0]["nodes"][1]["properties"]["squarish"]["url"] if shoe["publishedContent"]["nodes"][0]["nodes"][1]["properties"] != {} else shoe["publishedContent"]["nodes"][0]["nodes"][4]["properties"]["squarish"]["url"]
    img_three = shoe["publishedContent"]["nodes"][0]["nodes"][2]["properties"]["squarish"]["url"] if shoe["publishedContent"]["nodes"][0]["nodes"][2]["properties"] != {} else shoe["publishedContent"]["nodes"][0]["nodes"][4]["properties"]["squarish"]["url"]
    img_four = shoe["publishedContent"]["nodes"][0]["nodes"][3]["properties"]["squarish"]["url"] if shoe["publishedContent"]["nodes"][0]["nodes"][3]["properties"] != {} else shoe["publishedContent"]["nodes"][0]["nodes"][4]["properties"]["squarish"]["url"]
    data.append({"id": id, "title": title, "category": category, "price": price, "color": color, "inStock": inStock, "category": category, "img_one": img_one,"img_two": img_two,"img_three": img_three,"img_four": img_four,})

df = pd.DataFrame(data)

df.to_csv('shoes_data.csv', index=False)

df.head()