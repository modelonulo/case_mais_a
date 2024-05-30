import json
from elasticsearch import Elasticsearch

def index_texts():
    es = Elasticsearch("https://localhost:9200", http_auth=("elastic", "3Nud3ranVl6FEVS_CHKs"), verify_certs=False)

    # Caminho para o arquivo JSON
    json_path = 'Exercícios.json'

    # Leitura do arquivo JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        exercicios = json.load(file)

    # Indexação
    for i, exercicio in enumerate(exercicios["content"]):
        if "_id" in exercicio:
            del exercicio["_id"]
        es.index(index='exercicios', id=i+1, document=exercicio)

    print("Exercícios indexados com sucesso!")
