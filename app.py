from src.search_engine import SearchEngine

def load_documents():
    with open("data/knowledge.txt", "r") as file:
        docs = file.readlines()
    docs = [doc.strip() for doc in docs if doc.strip()]
    return docs


def main():
    print("AI Knowledge Assistant")

    documents = load_documents()

    engine = SearchEngine()
    engine.index_documents(documents)

    while True:
        query = input("\nAsk a question (or type exit): ")

        if query.lower() == "exit":
            break

        results = engine.search(query)

        print("\nRelevant Knowledge:")
        for r in results:
            print("-", r)


if __name__ == "__main__":
    main()