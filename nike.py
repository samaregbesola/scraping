import requests
import json
import pandas as pd


# url = "https://api.nike.com/cic/browse/v2"

# querystring = {"queryid":"products","anonymousId":"C8F8C0F14B39070F06EB813DBAC3F4CC","country":"us","endpoint":"/product_feed/rollup_threads/v2?filter=marketplace(US)&filter=language(en)&filter=employeePrice(true)&filter=attributeIds(16633190-45e5-4830-a068-232ac7aea82c,8529ff38-7de8-4f69-973c-9fdbfb102ed2)&anchor=0&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=60","language":"en","localizedRangeStr":"{lowestPrice} — {highestPrice}"}

# payload = ""
# headers = {"cookie": "_abck=905A957E3302B3898792D28C891F0E57~-1~YAAQHvEgF0aXewaJAQAAgKrhJApYani4OxkpkN6y0mBC4LsylbaKKQa5RULYggtr7qa5wC%2FeAYCG1mqfckFFa1UsBwWb7Vl02OTHnKB0imoCwLk4h6M1eTvXCnCPZjvkxKxAOajJB%2FZZTOqYGrVrjjxBbk9m%2FKL%2B67wCYE3Pt52FtULFl6bSdrurVYORkBKEcN2H52MJcKibSnBH%2BV6jW2xvNqVp%2BVyGxdTNb%2BF5AvrBCGUSkl1LYe5tQIXjC3dYNA4TfhWZfW2ciPJUrP2YCKRs%2FMC%2Bha4nuomeUbJq72AZ0MLpts8%2Bwtm591fCFseu%2BRpJR6GiegjXPaT7zOsCHER8mGO4QmL5A3ymwdlsQs29XrcfT3Smf5vNdFfp3oTq2%2Bl3tyML0TwHs4Oy6fACfJDXnr9o5PdZytLzKk6TSuOHjjpuL%2F0TfABhg25gziTVA9lEovVs62tQeRinB0UyQ5TiRIkZQuPrS5SsIP24NrldkCJzhg%3D%3D~-1~-1~-1; ak_bmsc=3576534D637A49C8A1446C864561639C~000000000000000000000000000000~YAAQP%2FEgF%2FsTZiSJAQAA7Lu%2BJBRY50wCUCfD%2Fuco8qaVY1asK2bnMU292I5PgbUj5g2LRiYEqYWjSnCJf%2BHZxZEcYP28Jk3icQ6LxagO3Lh0TSoOH6kpDlovTwP9IVeE2Kivx%2F9K6KAeYWh0RjYQ01BG%2Fj8hrPHW88T4%2F2p0D392NSX%2BOgBvADEoSCWQNgugs3NFWvCD9v0j37OtBv8t6tpGQcK5K6Erc0%2BOynQ59ws5AGICi9k8hFD2xziUQ%2F0o0HyyvQQRnRf85c0Y83jIa5pz265qsz%2F1dfj4%2B%2BivFDXExWAhRpOb4XQXmHWtLlaqZvQEfjmFbwzgZDXDeX0WkWIs1VtW%2BelNozRT0rdJrMRZPoGJLKVn%2BeYjhevnB%2FyB0RtIHrzlxj564A%3D%3D; bm_sv=C6BAE7CCC3A17621C1694410B6A8BA8E~YAAQdPEgF58rqROJAQAAybnZJBSBZpAT6w88BuMlMDuJKm%2F3d4PC9PftPtkzjpPy%2FcCxmC1PQkIOOW3tX%2FDSy9GGkpB9dY8Gi1y0TydCUcBjeu3ZdMpnY1LxgsBlaFH%2B6wPQVUGvmhW7xVkqmz05Pr3QZ6a1yOld3Gwo%2FzKwV9c1kDf1ENdoM%2FKn6wPVdDqP5LbLw%2BCPXy65Jl1bwYlB35YirTLmC%2B6xySKtAb7AuiaQKsqBcae1feRaxUAQ3vw%3D~1"}

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# json_data = json.loads(response.text)

# shoes = json_data['data']['products']['products']

# url = "https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=C8F8C0F14B39070F06EB813DBAC3F4CC&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C8529ff38-7de8-4f69-973c-9fdbfb102ed2)%26anchor%3D0%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D50&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D"

shoes = []
anchor = 0
fetching = True

while fetching:
    url = f"https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=C8F8C0F14B39070F06EB813DBAC3F4CC&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C8529ff38-7de8-4f69-973c-9fdbfb102ed2)%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D50&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D"
    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    shoes += json_data['data']['products']['products']
    print(shoes)
    if json_data['data']['products']['pages']['next'] != '':
        anchor += 50
    else:
        fetching = False




# process the shoes data
shoes

data = []
for shoe in shoes:
    id = shoe['pid']
    title = shoe['title']
    image = shoe['images']['squarishURL']
    price = shoe['price']['currentPrice']
    inStock = shoe['inStock']
    category = shoe['subtitle']
    isNew = shoe["colorways"][0]["isNew"]
    data.append({"id": id, "title": title, "image": image, "price": price, "inStock": inStock, "category": category, "isNew": isNew})

df = pd.DataFrame(data)

df.to_csv('shoes_data.csv', index=False)

df.head()
