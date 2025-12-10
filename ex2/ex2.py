class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CapaciteDepasseeException(ReservationException): pass
class NombreInvalideException(ReservationException): pass
class NomClientInvalideException(ReservationException): pass

class Evenement:
    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    def reserver(self, nom_client, nb_places):
        if not nom_client.strip():
            raise NomClientInvalideException("Nom du client requis.")
        if nb_places <= 0:
            raise NombreInvalideException("Nombre de places invalide.")
        if self.places_reservees + nb_places > self.capacite:
            raise CapaciteDepasseeException("Capacité dépassée.")

        self.places_reservees += nb_places
        print(f"Réservation confirmée pour {nom_client} ({nb_places} places).")

    def afficher(self):
        print(f"Événement: {self.nom} — {self.places_reservees}/{self.capacite} places réservées")

if __name__ == "__main__":
    event = Evenement("Show", 6)

    essais = [
        ("", 1),
        ("Ahmed", 7),
        ("Khalid", -2),
        ("Wissem", 3),
        ("Samir", 3),
        ("Taha", 1)
    ]

    for nom, nb in essais:
        try:
            event.reserver(nom, nb)
        except ReservationException as e:
            print("Erreur:", e)

    event.afficher()