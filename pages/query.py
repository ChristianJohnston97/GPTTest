from tempfile import NamedTemporaryFile

import openai
import streamlit as st
from openai import OpenAI

# Main Header and config
st.set_page_config(layout="wide")
# Styling
with open('style.css') as f:
    st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)


client = OpenAI()

st.write("""### Upload your digital advertiser RFP brief here... """)
uploaded_file = st.file_uploader("")
if uploaded_file is not None:
    with NamedTemporaryFile(dir='.', suffix='.txt') as tempFile:
        tempFile.write(uploaded_file.getbuffer())
        # file = client.files.create(
        #     file=open(tempFile.name, "rb"),
        #     purpose='assistants'
        # )
        assistant = client.beta.assistants.create(
            name="RFP reader",
            instructions="You are a publisher sales person. Your job is to extract all the key information from a digital advertiser RFP brief including key targeting information such as demographics and target segments",
            tools=[{"type": "retrieval"}],
            model="gpt-4-1106-preview",
            file_ids=[file.id]
        )




# loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
# data = loader.load()
# 
# 
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
# all_splits = text_splitter.split_documents(data)
# vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())
# question = "What are the approaches to Task Decomposition?"
# docs = vectorstore.similarity_search(question)
# print(docs)
