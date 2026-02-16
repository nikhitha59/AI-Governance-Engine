from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma(persist_directory="policy_db", embedding_function=embedding)

def retrieve_policy_context(query: str) -> str:
    docs = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])
