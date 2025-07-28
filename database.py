from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_anthropic import ChatAnthropic 
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.5)
database = SQLDatabase.from_uri("postgresql+psycopg2://postgres:admin@localhost/Ai_agent",
include_tables=['inventory','products','sales','suppliers'])
toolkit = SQLDatabaseToolkit(db=database, llm=llm)
agent = create_sql_agent(llm, toolkit, verbose=True)

# conn = psycopg2.connect(
#     host="localhost",
#     database="Ai_agent",
#     user="postgres",
#     password="admin"
# )



st.title("SQL Agent")
st.write("### Question")
question = st.text_input("Question:","after sold Product-001 how many quantity in stock?")

st.write(agent.invoke(question))

