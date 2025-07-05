from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_splitter():
    return RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=70)
