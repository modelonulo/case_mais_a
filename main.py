from index_texts import index_texts
from index_pdfs import index_pdfs
from index_videos import index_videos
from index_images import index_images

if __name__ == "__main__":
    print("Indexando textos...")
    index_texts()
    print("Indexando PDFs...")
    index_pdfs()
    print("Indexando vídeos...")
    index_videos()
    print("Indexando imagens...")
    index_images()
    print("Indexação concluída com sucesso!")
