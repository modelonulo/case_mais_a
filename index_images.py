from config import es

def index_images():
    # Metadados da imagem (para o MVP, manualmente definidos)
    imagem_metadados = {
        'filename': 'Infografico-1.jpg',
        'description': 'Infográfico explicativo sobre o tema.',
        'tags': ['infográfico', 'educação', 'tema']
    }

    # Indexação
    es.index(index='imagens', id=1, document=imagem_metadados)

    print("Imagem indexada com sucesso!")
