# Documentação Projeto de Aprendizagem Adaptativa

Este projeto visa criar um sistema de aprendizagem adaptativa utilizando um conjunto de dados relacionados aos fundamentos de programação. O objetivo é indexar diferentes tipos de dados e desenvolver um prompt que gere conteúdos dinâmicos conforme as dificuldades e desconhecimentos. Para este exemplo, indexei o conteúdo fornecido, mas trabalhei com a criação de conteúdo por uma LLMs usando o material do livro em pdf. No caso do vídeo, usaria Visual Language Models, por exemplo.

## Decisão da Arquitetura Utilizada

Optei por uma arquitetura simples apenas para exemplo a nível deste case, composta pelos seguintes componentes:

- **Elasticsearch**: Para indexar e buscar os dados textuais, PDFs, vídeos e imagens.
- **Python com Flask**: Para criar uma API que serve como backend do sistema.
- **OpenAI GPT 4o**: Para gerar conteúdos explicativos com base nos dados indexados.
- **Docker**: Para executar o Elasticsearch localmente, garantindo um ambiente controlado e facilmente replicável.

Essa arquitetura foi escolhida para garantir escalabilidade, facilidade de implementação e eficiência na busca e geração de conteúdos dinâmicos, mas é apenas um exemplo.

## Lista de Bibliotecas de Terceiros Utilizadas

- **Elasticsearch-py**: Biblioteca oficial do Elasticsearch para Python, utilizada para interagir com o Elasticsearch.
- **Flask**: Framework web utilizado para criar a API backend.
- **pdfplumber**: Biblioteca utilizada para extrair texto de arquivos PDF.
- **OpenAI**: Biblioteca para interagir com a API do GPT-3 da OpenAI.
- **ffmpeg-python**: Biblioteca para manipulação de arquivos de vídeo (não totalmente implementada neste projeto).
- **speechrecognition**: Biblioteca para transcrição de áudio (não totalmente implementada neste projeto).

## O que Você Melhoraria se Tivesse Mais Tempo

- **Integração Completa dos Vídeos**: Implementar a transcrição de vídeos e integração com o sistema de aprendizagem adaptativa.
- **Conteúdo Dinâmico para Exercícios**: Expandir o sistema para gerar conteúdos dinâmicos também para os exercícios indexados.
- **Interface de Usuário**: Criar uma interface web mais intuitiva e interativa para os usuários interagirem com o sistema de aprendizagem adaptativa.
- **Testes Automatizados**: Implementar testes automatizados para garantir a robustez e confiabilidade do sistema.

## Requisitos Obrigatórios que Não Foram Entregues

Não fiz uma interface de integração para uso direto do usuário (front). No mais, os requisitos obrigatórios foram entregues. A única limitação foi a não continuidade na criação de conteúdos dinâmicos com base nos vídeos e exercícios por uma questão de tempo disponível.

## Como Executar o Projeto

### Pré-requisitos

- Docker
- Python 3.10+
- Chave de API da OpenAI

### Passos para Executar
#### Clone o repositório:
#### Inicie o Elasticsearch usando Docker:
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.13.4
docker run --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.13.4
#### Instale as dependências do Python:
pip install -r requirements.txt
#### Configure a chave de API do OpenAI:
No terminal, execute antes de rodar: export OPENAI_API_KEY=“sua_chave_da_openai” 
#### Execute o script principal:
python main.py




