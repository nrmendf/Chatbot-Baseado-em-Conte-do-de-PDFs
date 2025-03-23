from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Vectorizer:
    def __init__(self, textos):
        self.vectorizer = TfidfVectorizer()
        self.matriz = self.vectorizer.fit_transform(textos)
        self.textos = textos

    def buscar_resposta(self, pergunta):
        pergunta_vetor = self.vectorizer.transform([pergunta])
        similaridades = cosine_similarity(pergunta_vetor, self.matriz)

        indice_mais_similar = similaridades.argmax()
        return self.textos[indice_mais_similar] if similaridades.max() > 0 else "Não encontrei uma resposta adequada."

