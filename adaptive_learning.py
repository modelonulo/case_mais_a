from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from config import es

from openai import OpenAI

client = OpenAI()


def get_user_input(prompt):
    return input(prompt)

def search_content(index, query):
    try:
        res = es.search(index=index, body={
            "query": {
                "match": {
                    "content": query
                }
            }
        })
        if res['hits']['hits']:
            return res['hits']['hits'][0]['_source']['content']
        return None
    except NotFoundError:
        print(f"O índice '{index}' não foi encontrado no Elasticsearch.")
        return None

def generate_explanatory_text(content, query):
    response = client.chat.completions.create(
        model="gpt-4o",
        #prompt=f"Use the following content to explain the concept of {query}:\n\n{content}",
        messages=[
            {"role": "system", "content": f"Use the following content to explain the concept of {query}. Content: {content}."},
            {"role": "user", "content": "{content}"}
        ],
        max_tokens=150
    )
    print(dir(response.choices[0]))
    return response.choices[0].message.content.strip()

def main():
    question = "O que você sabe sobre desenvolvimento de sistemas PHP?"
    index = "pdfs"
    
    print(question)
    user_answer = get_user_input("Sua resposta: ")
    
    # Buscar conteúdo relevante no Elasticsearch
    content = search_content(index, question)
    
    if content:
        # Gerar texto explicativo usando LLM
        explanatory_text = generate_explanatory_text(content, question)
        print(f"\nConteúdo explicativo:\n{explanatory_text}")
    else:
        print("Desculpe, não encontrei nenhuma informação relevante.")

if __name__ == "__main__":
    main()