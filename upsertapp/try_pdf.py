import pandas as pd
import json

def parsing_pdf(file_path):
    df = pd.read_csv(file_path)
    # test = df.head(10)
    sentences = []
    for index, row in df.iterrows():
        product_name = row['Product Name']
        ref = row['Ref./Art.']
        length = row['Length']
        diameter = row['Diameter']
        groove_type = row['Groove Type']
        bore = row['Bore']
        available_in = row['Available In']
        sentences.append(f'Products whose name is {product_name} have product which Ref./Art. is {ref}, Length is  {length}, Diameter is {diameter}, Groove Type is {groove_type}, Bore is {bore} and Available In is {available_in} val')
    
    print(len(sentences))
    return sentences


def parsing_shopify(file_path):

    df = pd.read_csv(file_path)

    test = df.head(10)

    sentences = []

    for index, row in df.iterrows():
        handle = row['Handle']
        title = row['Title']
        vendor = row['Vendor']
        published = row['Published']
        option1_name = row['Option1 Name']
        option1_value = row['Option1 Value']
        sentences.append(f'Products with Title is {title} and Handle is http://www.hectool.com/products/{handle} have product which its Vendor is {vendor},  Published is {published}, Option1_Name is {option1_name} and Option1_Value is {option1_value}')
    print(len(sentences))
    return sentences


def parse_pdf_json(path):
    df = pd.read_csv(path)
    data = []
    for index, row in df.iterrows():
        product_name = row['Product Name']
        ref = row['Ref./Art.']
        length = row['Length']
        diameter = row['Diameter']
        groove_type = row['Groove Type']
        bore = row['Bore']
        available_in = row['Available In']
        each = {
            "Title" : product_name,
            "Ref./Art." : ref,
            "Length" : length,
            "Diameter" : diameter,
            "Groove Type" : groove_type,
            "Bore" : bore,
            "Available In" : available_in,
        }
        data.append(json.dumps(each))
    return data

def parse_shopify_json(path):
    df = pd.read_csv(path)
    data = []
    for index, row in df.iterrows():
        handle = row['Handle']
        title = row['Title']
        vendor = row['Vendor']
        published = row['Published']
        option1_name = row['Option1 Name']
        option1_value = row['Option1 Value']
        each = {
            "Product Link" : handle,
            "Title" : title,
            "Vendor" : vendor,
            "Published" : published,
            "Option1 Name" : option1_name,
            "Option1 Value" : option1_value
        }
        data.append(json.dumps(each))
    return data