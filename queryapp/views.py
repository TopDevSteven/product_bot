from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
import json
import traceback
import openai
import pinecone
from .query_json import *
# Create your views here.


apiKey = config("OPENAI_API_KEY")
openai.api_key = apiKey

pinecone.init(
    api_key=config('PINECONE_API_KEY'),
    environment=config('PINECONE_ENV')
    )
active_indexes = pinecone.list_indexes()
index = pinecone.Index(active_indexes[0])

chat_history = []

def home(request):
    context = { }
    return render(request, "index.html", context)

def chat(request):
    if request.method == "POST":
        query = json.loads(request.body)
        print(query)
        query_res = query_embedding([query['query']])
        print(query_res)
        if not query_res:
            return JsonResponse({"message": "Querying Embedding Error!!!"})
        basedon_content = []
        json_lists = ""
        for i in query_res["matches"]:
            basedon_content.append(i["metadata"]["content"])
        basedon_content = get_uniquedata_shopify(basedon_content)
        print(basedon_content)
        for i in basedon_content:
            json_lists += i
        json_lists = limit_string_tokens(json_lists, 2000)
        assistant = "You should be an assistant of the marketplace Hectool, here you have to answer like real human, not like openai, model."
        chat_history.append({'role': 'user', 'content': json_lists})
        chat_history.append({'role': 'user', 'content': query['query']})
        total_tokens = sum([len(m["content"].split()) for m in chat_history])
        while total_tokens > 4000: # slightly less than model's max token limit for safety
            removed_message = chat_history.pop(0)
            removed_message = chat_history.pop(0)
            total_tokens -= len(removed_message["content"])
        try:
            res = openai.ChatCompletion.create(
                model = "gpt-4",
                temperature = 0.9,
                messages = [
                    {"role": "system", "content" : assistant},
                    {"role": "user", "content": "Hello!"},
                    {"role": "assistant", "content": "Hi there! I am your Hectool assistant today, how can I help?"},
                    {"role": "user", "content": "I am looking for clamping heads"},
                    {"role": "assistant", "content": "What type of clamping heads are you looking for? Or for what type of machine? Tell me more so I can help you find the correct product!"},
                    *chat_history
                ]
            )
            result = res["choices"][0]["message"]["content"]
            chat_history.append({"role": "assistant", "content": result})
            return JsonResponse({"message": result})
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"message": "Net Error"})

def create_embedding(content):
    try:
        res = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=content
        )
        print(res)
        embedding =  []
        vec_indexes = []
        idx = 0
        for i in res['data']:
            idx += 1
            embedding.append(i['embedding'])
            vec_indexes.append('vec' + str(idx))
        return content, embedding, vec_indexes
    except Exception as e:
        print(traceback.print_list)
        return JsonResponse({'message': 'Embedding Error!!!'})

def query_embedding(question):
    contents , embeddings, vec_idxs = create_embedding(question)
    if len(embeddings) == 0:
        return False
    try:
        query_res = index.query(
            namespace="machinetoolbot",
            top_k=50,
            include_values=True,
            include_metadata=True,
            vector=embeddings[0]
        )
        return query_res
    except Exception as e:
        print(traceback.format_exc())
        return False
        

def limit_string_tokens(string, max_tokens):
    tokens = string.split()
    if len(tokens) <= max_tokens:
        return string
    limited_string = ' '.join(tokens[:max_tokens])
    return limited_string