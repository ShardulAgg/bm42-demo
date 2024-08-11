from qdrant_client import QdrantClient

def init_script():
    qdrant = QdrantClient(":memory:")
    qdrant = QdrantClient("http://localhost:6333")
    
def upload_references(file_path):
    pass

def search(query):
    pass