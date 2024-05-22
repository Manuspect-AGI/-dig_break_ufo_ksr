import chromadb
import requests
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import pandas as pd
import uuid

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(
    # api_key='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', 
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load the data
data = pd.read_excel('/home/dukhanin/sim ds karpov/unique_naimenovanie_with_codes_dataset.xlsx')

# Initialize Chroma client
chroma_client = chromadb.HttpClient(host="localhost", port=8000)

# vectorstore = Chroma.from_texts(client=chroma_client, embedding=embeddings, texts=[data['Наименование'][i] for i in range(200)])

collection = chroma_client.create_collection(name="my_test_collection", embedding_function=embeddings)

for i in range(100):
    uuid_val = uuid.uuid1()
    # print("Inserted documents for ", uuid_val)
    collection.add(ids=[str(uuid_val)], documents=data['Наименование'][i], metadatas=data['Код ресурса'][i])


# # Add texts to vectorstore with error handling
# try:
#     texts = [x for x in data['Наименование']]
#     vectorstore = Chroma.from_texts(
#         client=chroma_client, 
#         embedding=embeddings, 
#         texts=texts
#     )
# except requests.exceptions.RequestException as e:
#     print(f"Request exception occurred: {e}")
# except requests.exceptions.JSONDecodeError as e:
#     print(f"JSON decode error: {e.msg}")
#     response_content = e.response.text if e.response else "No response content"
#     print(f"Response content: {response_content}")
# except Exception as e:
#     print(f"An error occurred: {e}")

# If adding documents, make sure to handle responses correctly
# for doc in data['Наименование']:
#     uuid_val = uuid.uuid1()
#     print("Inserted documents for ", uuid_val)
#     collection.add(ids=[str(uuid_val)], documents=doc)
