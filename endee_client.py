
import numpy as np

class EndeeClient:
    def __init__(self):
        self.vectors = []
        self.metadata = []

    def insert(self, id, vector, metadata):
        self.vectors.append(vector)
        self.metadata.append(metadata)

    def search(self, query_vector, top_k=5):
        sims = []
        for i, v in enumerate(self.vectors):
            sim = self.cosine_similarity(query_vector, v)
            sims.append((sim, self.metadata[i]))

        sims.sort(reverse=True, key=lambda x: x[0])
        return [{"score": s[0], "metadata": s[1]} for s in sims[:top_k]]

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
