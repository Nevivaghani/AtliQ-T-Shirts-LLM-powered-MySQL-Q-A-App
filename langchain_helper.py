import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI 
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import SQL_PROMPTS
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from few_shots import few_shots

load_dotenv()



def get_few_shot_db_chain():
    llm =  GoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_API_KEY"), model = "gemini-1.5-pro-latest", temperature = 0.2)

    db_user = "root"
    db_password = os.getenv("MYSQL_PASSWORD", "")
    db_host = "localhost"
    db_name = "atliq_tshirt_new"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

    to_vectorize = [" ".join(str(value) for value in example.values()) for example in few_shots]


    vecotrstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vecotrstore,
        k = 2
    )

    example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)
    custom_prefix = """You are an expert MySQL assistant.
    Given an input question, create a syntactically correct MySQL query to run.
    Execute the query using the given database and return the final answer based on the result.
    Provide the answer in plain English, not just the SQL query.
    """

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=custom_prefix,
        # suffix="\nQuestion: {input}\nSQLQuery:",
        suffix="\nQuestion: {input}\nSQLQuery:",
        input_variables=["input", "table_info", "top_k"]
    )

    # chain =  SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt= few_shot_prompt, return_intermediate_steps=False, return_direct=False)

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt, return_direct=True)

    return chain


if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    # print(chain.run("How many white color Levi shirt I have?"))
