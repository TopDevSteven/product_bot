from django.shortcuts import render
import openai
import pinecone
import traceback
from django.http import JsonResponse
from decouple import config

pinecone.init(api_key=config('PINECONE_API_KEY'),
                    environment=config('PINECONE_ENV'))
# Create your views here.
def create_embedding(content):
    try:
        res = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=content[0:1300]
        )
        embedding =  []
        vec_indexes = []
        metadata = []
        idx = -1
        for i in res['data']:
            idx += 1
            embedding.append(i['embedding'])
            vec_indexes.append('vec' + str(idx))
            metadata.append({'content': content[idx]})
        return metadata, embedding, vec_indexes
    except Exception as e:
        print(traceback.print_list)
        return JsonResponse({'message': 'Embedding Error!!!'})


def upsert_embedding(vector):
    try:
        active_indexes = pinecone.list_indexes()
        if len(active_indexes) != 0:
            index = pinecone.Index(active_indexes[0])
            print(active_indexes[0])
            try:
                vectors_list = chunk_list(vector, 50)
                for i in vectors_list:
                    index.upsert(vectors=i, namespace='machinetoolbot')
                print("successful upserting")
            except Exception as e:
                print(traceback.format_exc())
        else:
            pinecone.create_index("example-index", dimension=1536)
        return True
    except Exception as e:
        print(traceback.format_exc())
        return False

def chunk_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def create_index(request):
    if request.method == "GET":
        pinecone.create_index("example-index", dimension=1536)
        return JsonResponse({"message": "Successfully creating Index of pincone"})


# contents = [
#     """
# The clamping heads with type of 52, of which the length is 46 and outer diameter is 79.3 has the following types:
# The products include a round with bore diameter of 4-52, clamping surface of smooth and range of 0,5mm, a hexagon with bore diameter of 8-45, clamping surface of radial grooves and range of 1 and a square with bore diameter of 8 - 36, clamping surface of radial grooves and range of 1. Their total SKU's is 159.
#     """,
#     """
# The clamping heads with type of 52, of which the length is 46 and outer diameter is 79.3 has the following products:
# The products include a round with bore diameter of 8-52, clamping surface of radial grooves and range of 0,5mm, a hexagon with bore diameter of 7-45, clamping surface of smooth and range of 1 and a square with bore diameter of 7 - 36, clamping surface of smooth and range of 1. Their total SKU's is 167.
#     """,
#     """
# The clamping heads with type of 52, of which the length is 46 and outer diameter is 79.3 has the following types:
# The products include a round with bore diameter of 11-52, clamping surface of radial + longitudinal grooves and range of 0,5mm, a hexagon with bore diameter of none value, clamping surface of none value and range of none value and a square with bore diameter of none value, clamping surface of none value and range of none value. Their total SKU's is 84.
#     """,
#     """
# The clamping heads with type of 52, of which the length is 46 and outer diameter is 79.3 has the following types: 
# The products include a round with bore diameter of 4-52, clamping surface of emergency collet and range of none value, a hexagon with bore diameter of none value, clamping surface of none value and range of none value and a square with bore diameter of none value, clamping surface of none value and range of none value. Their total SKU's is 98.
# The total sum of upper products is 508.
#     """,
#     """
# The clamping heads with type of 65, of which the length is 53 and outer diameter is 99.5 has the following types: 
# The products include a round with bore diameter of 4-65, clamping surface of smooth and range of 0,5mm, a hexagon with bore diameter of 7 - 56, clamping surface of smooth and range of 1 and a square with bore diameter of 7 - 46, clamping surface of L and range of 1. Their total SKU's is 214.
#     """,
#     """
# The clamping heads with type of 65, of which the length is 53 and outer diameter is 99.5 has the following types: 
# The products include a round with bore diameter of 8-65, clamping surface of radial grooves and range of 0,5mm, a hexagon with bore diameter of 8 - 56, clamping surface of radial grooves and range of 1 and a square with bore diameter of 8 - 46, clamping surface of R and range of 1. Their total SKU's is 204.
#     """,
#     """
# The clamping heads with type of 65, of which the length is 53 and outer diameter is 99.5 has the following types: 
# The products include a round with bore diameter of 11-65, clamping surface of radial + longitudinal grooves and range of 0.5, a hexagon with bore diameter of none value, clamping surface of none value and range of none value and a square with bore diameter of none value, clamping surface of none value and range of none value. Their total SKU's is 110.
#     """,
#     """
# The clamping heads with type of 65, of which the length is 53 and outer diameter is 99.5 has the following types: 
# The products include a round with bore diameter of 4-65, clamping surface of emergency collet and range of none value, a hexagon with bore diameter of none value, clamping surface of none value and range of none value and a square with bore diameter of none value, clamping surface of none value and range of none value. Their total SKU's is 63.
#     """,
#     """
# The clamping heads with type of 65, of which the length is 58 and outer diameter is 99.5 has the following types:
# The products include a round with bore diameter of 4-65, clamping surface of smooth and range of 0,5mm, a hexagon with bore diameter of 7 - 56, clamping surface of L and range of 1 and a square with bore diameter of 7 - 46, clamping surface of smooth and range of 1. Their total SKU's is 214.
#     """,
#     """
# The clamping heads with type of 65, of which the length is 58 and outer diameter is 99.5 has the following types:
# The products include a round with bore diameter of 8-65, clamping surface of radial grooves and range of 0,5mm, a hexagon with bore diameter of 8 - 56, clamping surface of radial grooves and range of 1 and a square with bore diameter of 8 - 46, clamping surface of R and range of 1. Their total SKU's is 204.
#     """,
#     """
# The clamping heads with type of 65, of which the length is 58 and outer diameter is 99.5 has the following types:
# The products include a round with bore diameter of 11-65, clamping surface of radial + longitudinal grooves and range of 0.5, a hexagon with bore diameter of none value, clamping surface of none value and range of none value and a square with bore diameter of none value, clamping surface of none value and range of none value. Their total SKU's is 110.
# The clamping heads with type of 65, of which the length is 58 and outer diameter is 99.5 has the following types:
# The total sum of upper products is 1119.
#     """,
#     """
# There are clamping heads with type of 52 and 65
#     """
# ]

from .try_pdf import *

def upsert(request):
    if request.method == "GET":
        try:
            # contents = parse_shopify_json("./csvFiles/clamping heads_shopify_products (1).csv")
            contents = parse_pdf_json("./csvFiles/clamping heads PDF (2) (1).csv")
            metadata, embedding, vec_indexes = create_embedding(contents)
            vector = list(zip(vec_indexes, embedding, metadata))
            isUpsertingEmbedding = upsert_embedding(vector)
            if not isUpsertingEmbedding:
                return JsonResponse({"message": "inserting embedding Error"})
            return JsonResponse({"message": "success"})
        except:
            return JsonResponse({"message": "Embedding Error"})