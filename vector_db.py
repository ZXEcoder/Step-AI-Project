import numpy as np
from sentence_transformers import SentenceTransformer
from pymilvus import (
    Collection, CollectionSchema, FieldSchema, DataType,
    Milvus, utility, IndexType, IndexParam
)

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
        else:
            print(f"Collection {self.collection_name} already exists.")
    
    def create_hnsw_index(self):
        if not utility.has_collection(self.collection_name):
            raise ValueError(f"Collection {self.collection_name} does not exist.")
        
        collection = Collection(name=self.collection_name)
        index_params = {
            "index_type": IndexType.HNSW,
            "metric_type": "L2",
            "params": {"M": 16, "efConstruction": 128}
        }
        collection.create_index(field_name="embedding", index_params=index_params)
        print("HNSW index created.")

    def add_data(self, data):
        texts = [item['text'] for item in data]
        urls = [item['url'] for item in data]
        embeddings = self.model.encode(texts)
        
        collection = Collection(name=self.collection_name)
        collection.insert([texts, embeddings.tolist(), urls])
        print("Data inserted into collection.")
    
    def search(self, query, top_k=10):
        query_embedding = self.model.encode([query])[0].tolist()
        
        collection = Collection(name=self.collection_name)
        search_params = {"index_type": IndexType.HNSW, "metric_type": "L2"}
        results = collection.search([query_embedding], "embedding", search_params, top_k)
        
        return results

if __name__ == "__main__":
    vector_db = VectorDB()
    vector_db.create_collection()
    vector_db.create_hnsw_index()
    # Load data and add to DB
