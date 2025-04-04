# 🧠 AtliQ T-Shirts: LLM-powered MySQL Q&A App

A conversational AI-powered Streamlit web app built using **LangChain**, **Google Gemini**, and **MySQL**, allowing users to ask natural language questions about a T-shirt inventory database. The system dynamically generates and executes SQL queries and presents answers in plain English.

---

## 🚀 Features

- 🤖 LLM-powered SQL generation using Google Gemini (via LangChain)
- 🔍 Semantic example retrieval using Chroma + HuggingFace Embeddings
- 📊 Real-time interaction with MySQL database
- 🧾 Clean UI built with Streamlit
- 🔐 Environment variables managed via `.env`

---


---

## 🧠 Tech Stack

- **LLM**: Google Gemini (`langchain-google-genai`)
- **Prompting**: Few-shot prompting using LangChain
- **Vector Store**: Chroma with HuggingFace Sentence Transformers
- **Frontend**: Streamlit
- **Database**: MySQL (via `pymysql`)
- **Environment Management**: `python-dotenv`
- **Dependency Manager**: Poetry

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone  https://github.com/Nevivaghani/AtliQ-T-Shirts-LLM-powered-MySQL-Q-A-App.git
cd new_llm_project

2. Create a .env File

GOOGLE_API_KEY=your_google_api_key
MYSQL_PASSWORD=your_mysql_password

3. Install Dependencies via Poetry
poetry install

4. Ensure MySQL is Running
Make sure the MySQL server is running and the database atliq_tshirt_new is available.

5. Run the Streamlit App
poetry run streamlit run main.py

---

❓ How It Works
User inputs a natural language question (e.g., "How many white Levi shirts are in stock?")

LangChain:

Uses ChromaDB to retrieve semantically similar few-shot examples

Constructs a prompt combining custom instructions + examples + user question

Gemini generates a SQL query

The query is executed on the MySQL DB

The result is returned in plain English

🧪 Example Questions
"How many red T-shirts are available?"

"What is the average price of Puma shirts?"

"Which brands have more than 20 items?"

---


