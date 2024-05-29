import json
from elasticsearch import Elasticsearch

def index_texts():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # Leitura do arquivo JSON
    with open('case_mais_a/Exercícios.json', 'r', encoding='utf-8') as file:
        exercicios = json.load(file)

    # Indexação
    for i, exercicio in enumerate(exercicios):
        es.index(index='exercicios', id=i+1, document=exercicio)

    print("Exercícios indexados com sucesso!")
