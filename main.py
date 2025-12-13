
from src.Document import Document, RedditDocument, ArxivDocument
from src.Corpus import Corpus

# ce script est le script principal pour tester la gestion du corpus
corpus = Corpus("MonCorpus")


doc1 = RedditDocument("Reddit Doc 1", "Alice", "2025-12-01", "url1", "Ceci est le texte du doc 1", comments=5)
doc2 = ArxivDocument("Arxiv Doc 1", ["Bob", "Charlie"], "2025-11-20", "url2", "Ceci est le texte du doc 2")

corpus.add_document(doc1)
corpus.add_document(doc2)


corpus.show_docs()


corpus.save("data/corpus.csv")
new_corpus = Corpus("CorpusChargé")
new_corpus.load("data/corpus.csv")
new_corpus.show_docs()
