from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

def main():
    chemin = "articles.csv"
    try:
        articles = charger_csv(chemin)
        print("Articles chargés :", articles)
    except FichierIntrouvableException as e:
        print("Erreur : fichier introuvable.")
    except LigneInvalideException as e:
        print("Erreur : ligne invalide détectée.")
    except PrixNegatifException as e:
        print("Erreur : prix négatif détecté.")

if __name__ == "__main__":
    main()
