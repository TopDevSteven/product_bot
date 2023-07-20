import json

def get_uniquedata_pdf(content_list):
    product_names = set(item["Product Name"] for item in content_list)
    # unique_items = [item for item in random_data if item["Product Name"] in product_names]
    unique_data = []
    for each_product in product_names:
        for each_random in content_list:
            if each_product == each_random['Title']:
                unique_data.append(each_random)
    if len(unique_data) <2:
        return content_list
    # for item in pos_data:
    #     product_name = item['Product Name']
    #     ref = item['Ref./Art.']
    #     length = item['Length']
    #     diameter = item['Diameter']
    #     groove_type = item['Groove Type']
    #     bore = item['Bore']
    #     available_in = item['Available In']
    #     result.append(f'Products whose name is {product_name} have product which Ref./Art. is {ref}, Length is  {length}, Diameter is {diameter}, Groove Type is {groove_type}, Bore is {bore} and Available In is {available_in}')
    
    return unique_data

def get_uniquedata_shopify(content_list):
    product_names = set(item["Title"] for item in content_list)
    unique_data = []
    for each_product in product_names:
        for each_random in content_list:
            if each_product == each_random['Title']:
                unique_data.append(each_random)
    
    if len(unique_data) <2:
        return content_list
    # for item in pos_data:
    #     url = item['Product Link']
    #     title = item['Title']
    #     vendor = item['Vendor']
    #     published = item['Published']
    #     option1_name = item['Option1 Name']
    #     option1_value = item['Option1 Value']
    #     result.append(f'Products whose Title is {title} and Product Url is {url} have product which its Vendor is {vendor},  Published is {published}, Option1_Name is {option1_name} and Option1_Value is {option1_value}')
    
    return unique_data