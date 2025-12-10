import os

class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(f"Le fichier '{chemin}' est introuvable.")

    articles = []
    with open(chemin, encoding="utf-8") as f:
        for i, ligne in enumerate(f, start=1):
            ligne = ligne.strip()
            if not ligne:
                continue  # Ignorer lignes vides

            colonnes = ligne.split(";")
            if len(colonnes) != 3:
                raise LigneInvalideException(f"Ligne {i} invalide : {ligne}")

            id_, nom, prix_str = colonnes

            try:
                prix = float(prix_str)
            except ValueError:
                raise LigneInvalideException(f"Ligne {i} : prix non numérique '{prix_str}'")

            if prix <= 0:
                raise PrixNegatifException(f"Ligne {i} : prix négatif ou nul ({prix})")

            articles.append({"id": id_, "nom": nom, "prix": prix})

    return articles
