from elasticsearch import Elasticsearch

def index_images():
    es = Elasticsearch("https://localhost:9200", http_auth=("elastic", "3Nud3ranVl6FEVS_CHKs"), verify_certs=False)

    # Metadados da imagem (para o MVP, manualmente definidos)
    imagem_metadados = {
        'filename': 'Infografico-1.jpg',
        'description': 'Infográfico explicativo sobre o tema.',
        'tags': ['infográfico', 'educação', 'tema']
    }

    # Indexação
    es.index(index='imagens', id=1, document=imagem_metadados)

    print("Imagem indexada com sucesso!")
