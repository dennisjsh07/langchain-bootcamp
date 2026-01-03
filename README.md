## Implementation of RAG using langchain

This project explains the architecture and Implementation of RAG.

## Similarity Search

### When similarity_search is performed

the steps are:

    1. Embed the query text
    2. Compare the query vector with stored vectors
    3. Rank vectors by distance
    4. Return the top-k closest documents

similarity_search depending on the vector DB and configuration.
| Vector DB | Default |
| --------- | ------------------- |
| Chroma | Cosine |
| FAISS | L2 or Inner Product |
| Pinecone | Configurable |
| Weaviate | Configurable |

Chroma uses cosine similarity internally for text embeddings.
That means:

- vectors are L2-normalized
- similarity is based on angle, not magnitude

Two vectors pointing in the same direction → high similarity

### Important nuance: similarity vs distance

Chroma (and LangChain) often work with distance, not similarity:

| Metric            | Meaning               |
| ----------------- | --------------------- |
| Cosine similarity | Higher = more similar |
| Cosine distance   | Lower = more similar  |

- distance = 1 - cosine_similarity

### Why cosine similarity is best for text

Cosine similarity:

- ignores vector length
- focuses on semantic direction
- works well with normalized embeddings

This is why:

- most sentence transformers
- OpenAI embeddings
- Ollama embedding models
  are optimized for cosine similarity.

### similarity_search_with_score

- Returned score:
- lower = better (distance)

  0.0 ≈ perfect match
