from langchain_helper import get_few_shot_db_chain 
import streamlit as st

st.title("AtliQ T Shirts: Database Q&A")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    result = chain.invoke({"query": question})  # result is likely a dict or str

    st.subheader("Raw result for debugging:")
    st.write(result)

    try:
        # If result is a list like [(Decimal('176'),)], extract number
        if isinstance(result, list) and len(result) > 0:
            answer = int(result[0][0])
        elif isinstance(result, dict) and "result" in result:
            answer = result["result"]
        else:
            answer = "No valid result found."
    except Exception as e:
        answer = f"Error: {e}"

    st.header("Answer:")
    st.write(answer)
