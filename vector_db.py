import numpy as np
from sentence_transformers import SentenceTransformer
from pymilvus import Collection, CollectionSchema, FieldSchema, DataType, Milvus, utility

class VectorDB:
    def __init__(self, milvus_host='localhost', milvus_port='19530', collection_name='web_data'):
        self.client = Milvus(host=milvus_host, port=milvus_port)
        self.collection_name = collection_name
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def create_collection(self):
        fields = [
            FieldSchema(name='text', dtype=DataType.VARCHAR, max_length=10000),
            FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, dim=384),
            FieldSchema(name='url', dtype=DataType.VARCHAR, max_length=1000)
        ]
        schema = CollectionSchema(fields, description="Web data")
        collection = Collection(name=self.collection_name, schema=schema)
        if not utility.has_collection(self.collection_name):
            collection.create()

    def add_data(self, data):
        texts = [item['text'] for item in data]
        urls = [item['url'] for item in data]
        embeddings = self.model.encode(texts)
        collection = Collection(name=self.collection_name)
        collection.insert([texts, embeddings.tolist(), urls])

if __name__ == "__main__":
    vector_db = VectorDB()
    vector_db.create_collection()
    # Load data and add to DB
