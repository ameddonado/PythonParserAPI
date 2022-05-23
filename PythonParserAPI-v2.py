import json
import urllib.request
import webbrowser

# user enters the dispensary number (located in the url of each dispensary menu) / ownerId
user_input = input("Enter Dispensary Number: ")
# user enters product category
category_select = input("Enter Category: ")
# user enters brand name to filter through list
brand_input = input("Brand Name: ")
# user enters desired file name with .csv extension
filename = input("Desired Filename: ")

# the url that leads to the api json for each menu
dispensary_url = "https://www.redactedurl.com/menu/api/{}".format(user_input) + "?menuproductPriceGroupId=1&source=menu"
# open url request
with urllib.request.urlopen(dispensary_url) as url:
    data = json.load(url)
    json_obj = json.dumps(data)
    print(dispensary_url)

    # create file and parse through data
    with open(filename, 'w') as f:
        for items in data['items']:
            name = items.get('title')
            image_product = items.get('image')
            isproductimg = items.get('isProductImage')
            brand = items.get('brand')
            cms_id = items.get('id')
            cms_link = "https://managed.redactedurl.com/product/edit?id=" + cms_id
            category = items.get('category')
            straintype = items.get('strainType')

            # if the category is (user input) then print and save to file
            if category == category_select and brand == brand_input and not isproductimg:
                webbrowser.open_new_tab(cms_link)
                print(name, brand, category, straintype, image_product, cms_link, sep=",", file=f)