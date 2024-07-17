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
        st.write("Data added to vector database.")

    query = st.text_input("Enter your query")
    if st.button("Get Answer"):
        retriever = Retriever()
        # Add code to retrieve relevant data from the database
        context = "Provide relevant context here"
        qa = QuestionAnswering()
        answer = qa.answer_question(query, context)
        st.write(f"Answer: {answer}")

if __name__ == "__main__":
    main()
