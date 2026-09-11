# 🎓 University Chatbot

An AI-based university chatbot built using a **Retrieval-Augmented Generation (RAG) approach** to provide relevant information from university-specific data.

The main goal of this project is to build a university assistant that can understand a student's query, search the university knowledge base, and return the most relevant information.

> **Project Status:** 🚧 In Development

---

## 📌 About The Project

Students often have to search through different university pages, documents, and resources to find simple information about programs, admissions, departments, faculty, and other university-related topics.

This project aims to solve that problem by creating a centralized AI-powered chatbot that can retrieve relevant information from university data.

The current version focuses on the **retrieval part of the RAG pipeline**. It converts university information into embeddings, stores them in a vector database, and retrieves the most relevant information when a user asks a question.

The project is still being improved, especially the answer-generation and accuracy parts.

---

## 🧠 How It Works

The current pipeline works in the following way:

```text
University Data
      ↓
Data Cleaning
      ↓
Text Chunking
      ↓
Sentence Embeddings
      ↓
ChromaDB Vector Database
      ↓
User Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Relevant University Information
```

The system uses semantic similarity instead of only matching exact keywords.

For example:

```text
User:
"What programs are offered by the university?"

        ↓

Convert query into embedding

        ↓

Search similar information in ChromaDB

        ↓

Return the most relevant university information
```

---

## 🚀 Current Features

* University-specific knowledge base
* Text cleaning and preprocessing
* Text chunking
* Semantic search
* Sentence Transformer embeddings
* ChromaDB vector database
* Top-K relevant document retrieval
* Streamlit-based chatbot interface
* JSON-based university dataset
* Local embedding model

---

## 🛠️ Technologies Used

| Technology            | Purpose                              |
| --------------------- | ------------------------------------ |
| Python                | Main programming language            |
| Sentence Transformers | Generate text embeddings             |
| `all-MiniLM-L6-v2`    | Embedding model                      |
| ChromaDB              | Vector database                      |
| Streamlit             | User interface                       |
| JSON                  | University dataset                   |
| Jupyter Notebook      | Data preparation and experimentation |

---

## 📂 Project Structure

```text
University-chatbot/
│
├── Aror_Chatbot_Dataset_cleaned.json
│
├── chatbot.py
│
├── getting_things_ready.ipynb
│
├── streamlit_app.py
│
└── .gitignore
```

### `chatbot.py`

Contains the main RAG retrieval pipeline.

It handles:

* Loading the embedding model
* Loading the university dataset
* Cleaning text
* Creating text chunks
* Generating embeddings
* Creating/loading the ChromaDB collection
* Performing semantic search
* Returning the most relevant results

### `getting_things_ready.ipynb`

Notebook used for preparing and working with the university dataset before integrating it into the chatbot.

### `Aror_Chatbot_Dataset_cleaned.json`

The cleaned university dataset used as the knowledge source for the chatbot.

### `streamlit_app.py`

Provides the user interface for interacting with the chatbot through Streamlit.

---

## ⚙️ RAG Pipeline

### 1. Data Preparation

University information is collected and stored in a structured JSON dataset.

The data is then cleaned to remove unnecessary spaces and formatting problems.

### 2. Text Chunking

Large text is divided into smaller chunks so that individual pieces of information can be retrieved more efficiently.

The current implementation uses a simple word-based chunking strategy.

### 3. Embedding Generation

Each text chunk is converted into a numerical vector using:

```text
all-MiniLM-L6-v2
```

These embeddings represent the semantic meaning of the text.

### 4. Vector Storage

The generated embeddings are stored in **ChromaDB**.

This allows the system to search for information based on semantic similarity.

### 5. Query Processing

When a user asks a question, the question is also converted into an embedding.

The system then compares the query embedding with the stored university information.

### 6. Retrieval

The system retrieves the most relevant results using the similarity search.

The current system retrieves the **Top 3** results.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/AliNawaz003/University-chatbot.git
```

Move into the project directory:

```bash
cd University-chatbot
```

Install the required Python libraries:

```bash
pip install sentence-transformers chromadb streamlit
```

---

## ▶️ Run The Chatbot

Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

After running the command, Streamlit will provide a local URL where you can interact with the chatbot.

---

## 📊 Current Limitations

This project is still under development.

The current version has some important limitations:

* The chatbot currently focuses mainly on **retrieval**.
* An LLM is not yet connected for advanced natural-language answer generation.
* Retrieval accuracy can still be improved.
* The current chunking method is relatively simple.
* The system does not yet have a sophisticated reranking mechanism.
* There is currently no evaluation framework for measuring retrieval accuracy.
* The knowledge base needs to be continuously improved and expanded.

These limitations are part of the current development stage of the project.

---

## 🔮 Future Improvements

The next versions of the project can include:

* Connect a local or API-based LLM
* Improve RAG answer generation
* Better chunking strategy
* Metadata-based retrieval
* Hybrid search
* Reranking of retrieved documents
* Retrieval evaluation using Recall@K and MRR
* Hallucination reduction
* Source/citation-based answers
* Conversation memory
* Multilingual support
* Improved Streamlit interface
* Deployment for real university use

The long-term goal is to move from a basic semantic retrieval system toward a more complete and reliable **production-ready university AI assistant**.

---

## 🎯 Project Goal

The goal of this project is not simply to create another chatbot.

The aim is to understand and implement the complete pipeline behind a **domain-specific AI assistant**, including:

```text
Data
 ↓
Preprocessing
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retrieval
 ↓
LLM
 ↓
Grounded Response
 ↓
Evaluation
```

This project is being developed as a practical implementation of **Natural Language Processing, Information Retrieval, Embeddings, Vector Databases, and Retrieval-Augmented Generation (RAG).**

---

## 👨‍💻 Author

**Ali Nawaz**

GitHub: [AliNawaz003](https://github.com/AliNawaz003)

---

## ⭐ Project Status

**Currently under active development.**

The retrieval pipeline is implemented, and future work will focus on improving retrieval quality, connecting an LLM, reducing hallucinations, and making the system more reliable for real-world university use.
