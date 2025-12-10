class Document:
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte
        self.type = "Document"

    def __str__(self):
        return f"{self.titre} ({self.auteur})"

    def display(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Date: {self.date}")
        print(f"URL: {self.url}")
        print(f"Texte: {self.texte[:100]}...")  # premiers 100 caractères


class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, comments=0):
        super().__init__(titre, auteur, date, url, texte)
        self.comments = comments
        self.type = "Reddit"

    def __str__(self):
        return f"Reddit: {self.titre} ({self.comments} commentaires)"

class ArxivDocument(Document):
    def __init__(self, titre, auteurs, date, url, texte):
        super().__init__(titre, ', '.join(auteurs), date, url, texte)
        self.co_auteurs = auteurs
        self.type = "Arxiv"

    def __str__(self):
        return f"Arxiv: {self.titre} ({len(self.co_auteurs)} auteurs)"
