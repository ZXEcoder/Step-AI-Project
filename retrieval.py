from transformers import BertTokenizer, BertModel
from rank_bm25 import BM25Okapi
import numpy as np
import torch

class Retriever:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')
        self.bm25 = None
        self.data = []

    def train_bm25(self, documents):
        tokenized_docs = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(tokenized_docs)
        
    def retrieve(self, query, top_k=10):
        tokenized_query = query.split()
        scores = self.bm25.get_scores(tokenized_query)
        top_indices = np.argsort(scores)[-top_k:]
        return [self.data[i] for i in top_indices]

    def encode_query(self, query):
        inputs = self.tokenizer(query, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).numpy()

if __name__ == "__main__":
    retriever = Retriever()
    retriever.train_bm25(["Example document text 1", "Example document text 2"])  # Replace with real data
    result = retriever.retrieve("example query")
    print(result)
