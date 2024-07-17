---

# 🌐 Web-Based Question Answering System

Welcome to the Web-Based Question Answering System! This project is designed to scrape, chunk, and analyze data from the NVIDIA CUDA documentation to provide accurate and relevant answers to user queries. It employs advanced techniques for data chunking, vector storage, hybrid retrieval, and re-ranking, all powered by a robust language model for generating responses.

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
- [Demo](#demo)

---

## 🚀 Features

- **Web Crawling**: 
  - Scrape data from the [NVIDIA CUDA Documentation](https://docs.nvidia.com/cuda/).
  - Retrieve data from sub-links up to 5 levels deep.

- **Data Chunking and Vector Database Creation**:
  - Chunk data based on semantic similarity and topic relevance.
  - Convert data into embedding vectors.
  - Store embedding vectors in a Milvus vector database using HNSW indexing.
  - Store relevant metadata, such as web-links of the extracted chunks.

- **Retrieval and Re-ranking**:
  - Implement query expansion techniques.
  - Use hybrid retrieval methods (BM25 and BERT/bi-encoder methods like DPR and Spider).
  - Re-rank retrieved data based on query relevance and similarity.

- **Question Answering**:
  - Pass retrieved and re-ranked data to an LLM for generating answers.
  - Utilize the LLaMA model from Hugging Face for accurate responses.

- **User Interface (Optional)**:
  - Provide a user interface using Streamlit or Gradio.
  - Allow users to input queries and display retrieved answers.

---

## 🛠 Prerequisites

- **Python**: Python 3.8 or higher.
- **Libraries**: Install the required Python libraries using `requirements.txt`.
- **Milvus**: Install and set up Milvus. Follow the [Milvus installation guide](https://zilliz.com/blog/getting-started-with-a-milvus-connection).
- **Hugging Face Token**: Obtain a token from [Hugging Face](https://huggingface.co) for accessing the LLaMA model.

---

## 📥 Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/question-answering-system.git
   cd question-answering-system
   ```

2. **Install Python Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Milvus**:
   Follow the [Milvus installation guide](https://zilliz.com/blog/getting-started-with-a-milvus-connection).

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your Hugging Face token:
   ```env
   HF_TOKEN=your_hugging_face_token
   ```

---

## 🚀 Usage

### Running the Web Crawler

Run the web crawler to scrape data from the NVIDIA CUDA documentation and store it in `chunked_data.json`:
```sh
python web_crawler.py
```

![Web Crawling](https://path/to/your/web_crawling.gif)

### Creating Vector Database and Inserting Data

Run the script to chunk the data and create a vector database:
```sh
python create_vector_db.py
```

![Vector Database Creation](https://path/to/your/vector_db_creation.gif)

### Running the Question Answering System

Run the main script for question answering:
```sh
python question_answering.py
```

![Question Answering](https://path/to/your/question_answering.gif)

### Running the User Interface (Optional)

Run the Streamlit app for the user interface:
```sh
streamlit run app.py
```

![User Interface](https://path/to/your/user_interface.gif)

---

## 📁 File Structure

```
question-answering-system/
│
├── web_crawler.py           # Script for web crawling and data scraping
├── create_vector_db.py      # Script for chunking data and creating vector database
├── question_answering.py    # Main script for question answering
├── app.py                   # Streamlit app for the user interface
├── requirements.txt         # List of required Python packages
└── .env                     # Environment variables
```

---

## 🤝 Contributing

We welcome contributions! To contribute, follow these steps:

1. **Fork the Repository**: Click on the 'Fork' button on the top right corner of this repository page.

2. **Clone the Forked Repository**:
   ```sh
   git clone https://github.com/yourusername/question-answering-system.git
   cd question-answering-system
   ```

3. **Create a New Branch**:
   ```sh
   git checkout -b your-feature-branch
   ```

4. **Make Changes and Commit**:
   ```sh
   git add .
   git commit -m "Add your commit message"
   ```

5. **Push Changes to GitHub**:
   ```sh
   git push origin your-feature-branch
   ```

6. **Submit a Pull Request**: Go to your forked repository on GitHub and click the 'New pull request' button.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Acknowledgements

- [Hugging Face](https://huggingface.co) for providing the LLaMA model.
- [Milvus](https://milvus.io) for the vector database solution.
- [Streamlit](https://streamlit.io) for the web application framework.

---

## 📧 Contact

If you have any questions or suggestions, feel free to open an issue or contact us directly.

---

## 📽 Demo

Here's a visual walkthrough of the system in action:

### Web Crawling

![Web Crawling](https://path/to/your/web_crawling.gif)

### Vector Database Creation

![Vector Database Creation](https://path/to/your/vector_db_creation.gif)

### Question Answering

![Question Answering](https://path/to/your/question_answering.gif)

### User Interface

![User Interface](https://path/to/your/user_interface.gif)

---

Thank you for using our Web-Based Question Answering System! 

---
