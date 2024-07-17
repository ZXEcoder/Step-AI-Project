import streamlit as st
from crawler import WebCrawler
from vector_db import VectorDB
from retrieval import Retriever
from qa import QuestionAnswering

def main():
    st.title("Web Data QA System")
    
    base_url = st.text_input("Enter base URL", "https://docs.nvidia.com/cuda/")
    if st.button("Start Crawling"):
        crawler = WebCrawler(base_url)
        scraped_data = crawler.crawl()
        st.write(f"Scraped {len(scraped_data)} pages.")

        vector_db = VectorDB()
        vector_db.create_collection()
        vector_db.add_data(scraped_data)
        vector_db.create_hnsw_index()

    query = st.text_input("Enter your query")
    if st.button("Get Answer"):
        retriever = Retriever()
        retriever.data = [item['text'] for item in scraped_data]  # Update with actual document texts
        retriever.train_bm25(retriever.data)
        
        search_results = vector_db.search(query)
        top_results = retriever.retrieve(query)
        
        context = "Provide relevant context here from top_results"
        qa = QuestionAnswering()
        answer = qa.answer_question(query, context)
        
        st.write(f"Answer: {answer}")

if __name__ == "__main__":
    main()
