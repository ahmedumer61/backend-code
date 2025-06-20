# Document RAG App Powered by Groq LLM

This project is a **Streamlit** web application that allows users to upload documents (PDF, Word, or text files), process their contents, and query them using a **Retrieval-Augmented Generation (RAG)** approach. The application leverages **Groq LLM (GPT-4o)** for accurate question-answering based on the uploaded documents.

---

## Features

- **Document Upload**: Supports PDF, DOC, DOCX, and TXT files.
- **Document Content Extraction**: Reads the content of the uploaded documents and processes it for querying.
- **Question Answering**: Users can ask questions about the uploaded documents, and the app generates context-aware answers.
- **Session Management**: Keeps track of uploaded documents and their content during the session.
- **Clear All Documents**: Allows clearing all uploaded documents from the session.
- **Real-Time Querying**: Provides instant responses powered by Groq LLM.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (saved in a `.env` file)
- Required Python packages (see `requirements.txt`)


## Create a virtual Environment
```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
## Install Dependencies:
```
pip install -r requirements.txt
```

## Run the Application:
```
streamlit run app.py
```