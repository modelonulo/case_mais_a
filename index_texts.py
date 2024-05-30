import json
from config import es

def index_texts():
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
