from langchain_community.document_loaders import PyPDFLoader,WebBaseLoader

def load_pdf_document(pdf):
    loader = PyPDFLoader(pdf)
    documents = loader.load()
    return documents

def load_url_document(url):
    web_loader = WebBaseLoader(url)
    web_url_documents = web_loader.load()
    return web_url_documents


def custom_prompt(qdrant, query: str):
    results = qdrant.similarity_search(query, k=5)
    source_knowledge = "\n".join([x.page_content for x in results])
    augment_prompt = f"""Using the contexts below, answer the query:

    Contexts:
    {source_knowledge}

    Query: {query}"""
    return augment_prompt
