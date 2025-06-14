def hybrid_search(query: str):
    cached = redis_vector_lookup(query)
    if cached:
        return cached
    return search_milvus(query)

def redis_vector_lookup(query):
    return None

def search_milvus(query):
    return [{"doc_id": "AML Guide", "score": 0.9}]
