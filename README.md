
# Web-Based Question Answering System

## Overview

This project is a sophisticated web-based question answering system designed to scrape, chunk, and analyze data from the NVIDIA CUDA documentation. The system utilizes advanced techniques for data chunking, vector storage, hybrid retrieval


# Web-Based Question Answering System

## Overview

This project is a sophisticated web-based question answering system designed to scrape, chunk, and analyze data from the NVIDIA CUDA documentation. The system utilizes advanced techniques for data chunking, vector storage, hybrid retrieval, and re-ranking to provide accurate and relevant answers to user queries.

## Features

1. **Web Crawling**
   - Scrapes data from the provided website: [NVIDIA CUDA Documentation](https://docs.nvidia.com/cuda/).
   - Retrieves data from sub-links up to 5 levels deep.
   - Identifies and scrapes data from both parent and sub-links.

2. **Data Chunking and Vector Database Creation**
   - Chunks the scraped data based on semantic similarity and topic relevance.
   - Converts the chunked data into embedding vectors.
   - Stores embedding vectors in a Milvus vector database using HNSW indexing.
   - Stores relevant metadata, such as the web-link of the extracted chunk.

3. **Retrieval and Re-ranking**
   - Implements query expansion techniques to enhance retrieval.
   - Utilizes hybrid retrieval methods combining BM25 and BERT/bi-encoder-based retrieval methods like DPR and Spider.
   - Re-ranks retrieved data based on relevance and similarity to the query.

4. **Question Answering**
   - Passes retrieved and re-ranked data to an LLM for generating answers.
   - Utilizes LLaMA model from Hugging Face for generating accurate and relevant answers.

5. **User Interface (Optional)**
   - Provides a user interface using Streamlit or Gradio for query input and answer display.

## Prerequisites

1. **Python**: Ensure you have Python 3.8 or higher installed.
2. **Libraries**:
   - `transformers`
   - `torch`
   - `pymilvus`
   - `requests`
   - `beautifulsoup4`
   - `langchain`
   - `streamlit` (if using the UI)

3. **Milvus**: Install and set up Milvus. Follow the [Milvus installation guide](https://zilliz.com/blog/getting-started-with-a-milvus-connection).

4. **Hugging Face Token**: Obtain a Hugging Face token for accessing the LLaMA model. You can get it from [Hugging Face](https://huggingface.co).

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/question-answering-system.git
   cd question-answering-system
   ```

2. **Install Python dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up Milvus**:
   Follow the [Milvus installation guide](https://zilliz.com/blog/getting-started-with-a-milvus-connection) to set up Milvus on your cloud or local machine.

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your Hugging Face token:
   ```env
   HF_TOKEN=your_hugging_face_token
   ```

## Usage

1. **Run the web crawler**:
   ```sh
   python web_crawler.py
   ```
   This will scrape data from the NVIDIA CUDA documentation and store it in `chunked_data.json`.

2. **Create Vector Database and Insert Data**:
   ```sh
   python create_vector_db.py
   ```

3. **Run the Question Answering System**:
   ```sh
   python question_answering.py
   ```

4. **(Optional) Run the User Interface**:
   ```sh
   streamlit run app.py
   ```

## File Structure

- `web_crawler.py`: Script for web crawling and data scraping.
- `create_vector_db.py`: Script for chunking data and creating vector database.
- `question_answering.py`: Main script for question answering.
- `app.py`: Streamlit app for the user interface.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment variables.

## Contributing

Contributions are welcome! Please create a pull request with detailed descriptions of the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co) for providing the LLaMA model.
- [Milvus](https://milvus.io) for the vector database solution.
- [Streamlit](https://streamlit.io) for the web application framework.
```

This `README.md` file includes an overview of the project, features, prerequisites, installation instructions, usage guidelines, file structure, contribution guidelines, license information, and acknowledgements. Adjust the GitHub repository link, Hugging Face token instructions, and any other specifics as needed.
