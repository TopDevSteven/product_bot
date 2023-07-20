import json

def get_uniquedata_shopify(content_list):
    unique_data_dict = {}
    for each_random in content_list:
        title = json.loads(each_random)['Title']
        unique_data_dict[title] = each_random

    unique_data = list(unique_data_dict.values())
    
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