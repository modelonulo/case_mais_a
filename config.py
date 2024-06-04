from elasticsearch import Elasticsearch

# Configuração global do Elasticsearch
es = Elasticsearch("https://localhost:9200", http_auth=("elastic", "3555Nud3ranVl6FEVS_CHKs"), verify_certs=False)
