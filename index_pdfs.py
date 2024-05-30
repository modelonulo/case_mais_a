import pdfplumber
from config import es

def index_pdfs():
    # Função para extrair texto de um PDF
    def extract_text_from_pdf(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            text = ''.join([page.extract_text() for page in pdf.pages])
        return text

    # Caminho para o PDF
    pdf_path = 'livro.pdf'

    # Extração e indexação
    pdf_text = extract_text_from_pdf(pdf_path)
    es.index(index='pdfs', id=1, document={'content': pdf_text, 'path': pdf_path})

    print("PDF indexado com sucesso!")
