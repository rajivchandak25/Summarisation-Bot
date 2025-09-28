from sentence_transformers import SentenceTransformer, util

# -------------------------------
# Retriever: ranks results with embeddings
# -------------------------------
class Retriever:
    def __init__(self):
        # Lightweight embedding model
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def rank_summaries(self, query: str, summaries: list):
        """
        Given a query and list of summaries, return the most relevant one.
        """
        if not summaries:
            return None

        query_emb = self.embedder.encode(query, convert_to_tensor=True)
        summary_embs = self.embedder.encode(summaries, convert_to_tensor=True)

        scores = util.pytorch_cos_sim(query_emb, summary_embs)[0]
        best_idx = scores.argmax().item()
        
        return summaries[best_idx]
