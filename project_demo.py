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

load_dotenv()

llm =  GoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_API_KEY"), model = "gemini-1.5-pro-latest", temperature = 0.2)

# poem = llm("Write a poem about the ocean")
# print(poem)

db_user = "root"
db_password = os.getenv("MYSQL_PASSWORD", "")
db_host = "localhost"
port = 3306
db_name = "atliq_tshirt_new"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
# print(db.table_info)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose= True)
# qns1 = db_chain("Return only the SQL query without formatting. How many t-shirts do we have left for Nike in extra small size and white color?")

# # print(qns1)


# qns2 = db_chain("Return only the SQL query without formatting. How much is the total price of inventory for all small size t-shirts?")
# # print(qns2)


# qns3 = db_chain("Return only the SQL query without formatting. If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue our store will generate (post discounts)?")
# # print(qns3)

# query = "SELECT stock_quantity FROM t_shirts WHERE brand = 'Nike' AND size = 'XS' AND color = 'White';"
# # result = db.run(query)
# # print(result)

# sql_code = """
# SELECT SUM(price * stock_quantity * (1 - COALESCE(discounts.pct_discount, 0) / 100)) AS total_revenue
# FROM t_shirts
# LEFT JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id
# WHERE brand = 'Levi';
# """

# qns4 = db_chain("Return only the SQL query without formatting. SELECT SUM(price * stock_quantity * (1 - COALESCE(discounts.pct_discount, 0) / 100)) AS total_revenue FROM t_shirts LEFT JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id WHERE brand = 'Levi';")
# # print(qns4)

# qns5 = db_chain("Return only the SQL query without formatting. How many white color Levi's t shirts we have available?")
# # print(qns5)

few_shots = [
    {'Question' : "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     'SQLResult': "Result of the SQL query",
     'Answer' : 51},
    {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
     'SQLQuery':"SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
     'SQLResult': "Result of the SQL query",
     'Answer': 21362},
    {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?" ,
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': 3176} ,
    #  {'Question' : "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?" ,
    #   'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
    #   'SQLResult': "Result of the SQL query",
    #   'Answer' : qns4},
    # {'Question': "How many white color Levi's shirt I have?",
    #  'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
    #  'SQLResult': "Result of the SQL query",
    #  'Answer' : qns5
    #  }
]

embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

# e = embeddings.embed_query("How many white color Levi's shirt I have?")
# print(len(e))

# to_vectorize = [" ".join(example.values()) for example in few_shots]
to_vectorize = [" ".join(str(value) for value in example.values()) for example in few_shots]


vecotrstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)

example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vecotrstore,
    k = 2
)

# print(example_selector.select_examples({"Question": "How many Adidas T shirts I have left in my store?"}))

# print(SQL_PROMPTS)

example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)

custom_prefix = """You are an expert MySQL assistant.
Given an input question, create a syntactically correct MySQL query to run.
Return only the SQL query, nothing else.

Here are some examples:
"""

# print(SQL_PROMPTS)
few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=custom_prefix,
    suffix="\nQuestion: {input}\nSQLQuery:",
    input_variables=["input", "table_info", "top_k"],
)

print(few_shot_prompt)

new_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt= few_shot_prompt, return_intermediate_steps=False, return_direct=False   )
# print(new_chain("How many white color Levi shirt I have?"))
# print(new_chain("How much is the price of the inventory for all small size t-shirts?"))
print(new_chain("If we have to sell all the Nike’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?"))