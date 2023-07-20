import json

def get_uniquedata_pdf(content_list):
    pos_data = []
    current_name = ''
    result = []
    for item in content_list:
        if json.loads(item)["Product Name"] == current_name:
            continue
        else:
            current_name = json.loads(item)["Product Name"]
            pos_data.append(item)
    if len(pos_data) < 2:
        pos_data = content_list
    # for item in pos_data:
    #     product_name = item['Product Name']
    #     ref = item['Ref./Art.']
    #     length = item['Length']
    #     diameter = item['Diameter']
    #     groove_type = item['Groove Type']
    #     bore = item['Bore']
    #     available_in = item['Available In']
    #     result.append(f'Products whose name is {product_name} have product which Ref./Art. is {ref}, Length is  {length}, Diameter is {diameter}, Groove Type is {groove_type}, Bore is {bore} and Available In is {available_in}')
    
    return pos_data

def get_uniquedata_shopify(content_list):
    pos_data = []
    current_name = ''
    for item in content_list:
        if json.loads(item)["Title"] == current_name:
            continue
        else:
            current_name = json.loads(item)["Title"]
            pos_data.append(item)
            # print(item)
    if len(pos_data) == 1:
        pos_data = content_list
    # for item in pos_data:
    #     url = item['Product Link']
    #     title = item['Title']
    #     vendor = item['Vendor']
    #     published = item['Published']
    #     option1_name = item['Option1 Name']
    #     option1_value = item['Option1 Value']
    #     result.append(f'Products whose Title is {title} and Product Url is {url} have product which its Vendor is {vendor},  Published is {published}, Option1_Name is {option1_name} and Option1_Value is {option1_value}')
    
    return pos_data