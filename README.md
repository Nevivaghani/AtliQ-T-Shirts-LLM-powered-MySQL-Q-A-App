# 🧠 AtliQ T-Shirts: LLM-powered MySQL Q&A App

A conversational AI-powered Streamlit web app built using **LangChain**, **Google Gemini**, and **MySQL**, allowing users to ask natural language questions about a MySQL database of AtliQ T-shirt inventory. The system generates and executes SQL queries based on user input and returns the results in plain English using few-shot prompting and semantic similarity.

---

## 🚀 Features

- 🤖 LLM-powered SQL generation with **Google Gemini**
- 🔍 Semantic example retrieval using **Chroma vector store**
- 📊 Real-time interaction with **MySQL database**
- 💡 Few-shot learning with semantic search using **HuggingFace embeddings**
- 🧾 Streamlit-based interactive UI
- 🔐 Environment variables handled securely using `.env`

---

## 📁 Project Structure

new_llm_project/ │ ├── main.py # Streamlit app ├── langchain_helper.py # LangChain setup with few-shot examples & vector store ├── few_shots.py # Few-shot example data (not shown here) ├── .env # Environment variables (GOOGLE_API_KEY, MYSQL_PASSWORD) ├── pyproject.toml # Poetry dependency manager └── README.md # Project documentation

markdown
Copy
Edit

---

## 🧠 Tech Stack

- **LLM**: Google Gemini (via `langchain-google-genai`)
- **Frameworks**: LangChain, Streamlit
- **Database**: MySQL (via `SQLAlchemy` + `pymysql`)
- **Vector Store**: ChromaDB with `HuggingFace sentence-transformers`
- **Prompt Engineering**: Few-shot learning with semantic similarity
- **Environment Management**: `python-dotenv`, `poetry`

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Nevivaghani/AtliQ-T-Shirts-LLM-powered-MySQL-Q-A-App.git
cd new_llm_project
2. Set up Environment Variables
Create a .env file:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key
MYSQL_PASSWORD=your_mysql_password
3. Install Dependencies
Use Poetry for dependency management:

bash
Copy
Edit
poetry install
4. Run MySQL Server
Ensure your MySQL server is running and that the database atliq_tshirt_new exists with relevant tables.

5. Start the App
bash
Copy
Edit
poetry run streamlit run main.py
❓How It Works
User enters a question in natural language (e.g., "How many white Levi’s shirts are available?")

The app uses Google Gemini to:

Select semantically similar few-shot examples using Chroma vectorstore

Generate an SQL query based on those examples and your schema

Execute it on the MySQL database

Return the result in plain English

📌 Example Questions
How many red T-shirts are in stock?

What is the average price of Puma shirts?

List all brands with more than 10 items.

🛠 To-Do / Improvements
✅ Add Gemini LLM integration

✅ Setup vector-based few-shot retrieval

🔲 Add error handling for malformed queries

🔲 UI enhancement with table previews

🔲 Dockerize the app for deployment

👤 Author
Nevivaghani
📧 nevivaghani793@gmail.com

📃 License
This project is licensed under the MIT License. See the LICENSE file for more info.

yaml
Copy
Edit

---

Let me know if you want to add badges, GIF demos, sample screenshots, or instructions for Docker setup next!






You said:
create single file 


ChatGPT said:
Absolutely! Here's your complete README.md content as a single Markdown file, ready to be saved directly as README.md in VS Code:

markdown
Copy
Edit
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

## 📁 Project Structure

new_llm_project/ ├── main.py # Streamlit frontend ├── langchain_helper.py # Chain setup and prompt logic ├── few_shots.py # Few-shot example data ├── .env # Stores API keys and DB passwords ├── pyproject.toml # Poetry dependency configuration └── README.md # You're reading it!

yaml
Copy
Edit

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
git clone https://github.com/yourusername/new_llm_project.git
cd new_llm_project
2. Create a .env File
ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key
MYSQL_PASSWORD=your_mysql_password
3. Install Dependencies via Poetry
bash
Copy
Edit
poetry install
4. Ensure MySQL is Running
Make sure the MySQL server is running and the database atliq_tshirt_new is available.

5. Run the Streamlit App
bash
Copy
Edit
poetry run streamlit run main.py
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

