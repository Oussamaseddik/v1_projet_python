
import pandas as pd
from src.Document import Document, RedditDocument, ArxivDocument
from src.Author import Author
#Structure centrale pour gerer les documents : ajouter des documents et son auteur et affichier les 1er docs du corpus
class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.id2doc = {}
        self.authors = {}
        self.ndoc = 0
        self.naut = 0

    def add_document(self, doc):
        doc_id = self.ndoc
        self.id2doc[doc_id] = doc
        self.ndoc += 1

  
        if doc.auteur not in self.authors:
            self.authors[doc.auteur] = Author(doc.auteur)
            self.naut += 1
        self.authors[doc.auteur].add(doc_id, doc)

    def show_docs(self, n=5):
        for i, doc in list(self.id2doc.items())[:n]:
            print(doc)
# recharger et sauvgarder le corpus dans un ficher 
    def save(self, filename):
        data = []
        for doc_id, doc in self.id2doc.items():
            data.append([doc_id, doc.titre, doc.auteur, doc.date, doc.url, doc.texte, doc.type])
        df = pd.DataFrame(data, columns=["id","titre","auteur","date","url","texte","type"])
        df.to_csv(filename, sep="\t", index=False)

    def load(self, filename):
        df = pd.read_csv(filename, sep="\t")
        for _, row in df.iterrows():
            if row['type'] == "Reddit":
                doc = RedditDocument(row['titre'], row['auteur'], row['date'], row['url'], row['texte'], comments=0)
            elif row['type'] == "Arxiv":
                doc = ArxivDocument(row['titre'], row['auteur'].split(','), row['date'], row['url'], row['texte'])
            else:
                doc = Document(row['titre'], row['auteur'], row['date'], row['url'], row['texte'])
            self.add_document(doc)
