from elasticsearch import Elasticsearch
import pdfplumber

def index_pdfs():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # Função para extrair texto de um PDF
    def extract_text_from_pdf(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            text = ''.join([page.extract_text() for page in pdf.pages])
        return text

    # Caminho para o PDF
    pdf_path = 'case_mais_a/Capítulo do Livro.pdf'

    # Extração e indexação
    pdf_text = extract_text_from_pdf(pdf_path)
    es.index(index='pdfs', id=1, document={'content': pdf_text, 'path': pdf_path})

    print("PDF indexado com sucesso!")
