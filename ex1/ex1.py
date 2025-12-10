class SoldeInsuffisantException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException("Solde insuffisant pour ce retrait.")
        self.solde -= montant

    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")

if __name__ == "__main__":
    try:
        compte = CompteBancaire("Alice", 100)
        compte.afficher()
        compte.retirer(150)
    except SoldeInsuffisantException as e:
        print("Erreur:", e)