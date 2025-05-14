from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
import os

VECTOR_DB_PATH = "chat_data/vector_store"

# Simulated document search (fallback if vector DB isn't used)
def search_documents(prompt):
    sample_data = {
        "solar cell": "A solar cell is a device that converts sunlight directly into electricity using the photovoltaic effect.",
        "kenya counties": "Here is a table of counties in Kenya and their populations:\nCounty\tPopulation\nNairobi\t4.4M\nMombasa\t1.2M\nKisumu\t1.1M\nNakuru\t2.1M\nEldoret\t1.0M"
    }
    for key, value in sample_data.items():
        if key in prompt.lower():
            return [value]
    return []

def query_vector_store(prompt, use_chat_history=True):
    try:
        matches = search_documents(prompt)

        if not matches:
            return "⚠️ No relevant documents found. Please upload more or try rephrasing your question."

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
        filter_prompt = f"""
        Question: {prompt}
        Raw Context: {matches[0]}

        Return a clear, direct answer to the question above using the provided context. If no match, say:
        '⚠️ No relevant answer found.'
        """
        response = llm.call_as_llm(filter_prompt)
        return response.strip()
    except Exception as e:
        return f"❌ Error processing query: {e}"

def train_on_csv(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"{csv_path} not found")

    loader = CSVLoader(file_path=csv_path)
    docs = loader.load()

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(VECTOR_DB_PATH)
