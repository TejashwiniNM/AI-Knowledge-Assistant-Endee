from src.embeddings import EmbeddingGenerator
from src.vector_store import VectorStore

class SearchEngine:
    def __init__(self):
        self.embedding_generator = EmbeddingGenerator()
        self.vector_store = VectorStore()

    def index_documents(self, texts):
        embeddings = self.embedding_generator.generate_embeddings(texts)
        self.vector_store.add(embeddings, texts)

    def search(self, query):
        query_embedding = self.embedding_generator.generate_embeddings([query])[0]
        results = self.vector_store.search(query_embedding)
        return results