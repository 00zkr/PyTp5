import unittest
import os
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

class TestCsvReader(unittest.TestCase):

    def setUp(self):
        with open("valid.csv", "w", encoding="utf-8") as f:
            f.write("1;Article A;10.5\n2;Article B;20\n3;Article C;5.75\n")

        with open("prix_text.csv", "w", encoding="utf-8") as f:
            f.write("1;Article A;abc\n")

        with open("prix_negatif.csv", "w", encoding="utf-8") as f:
            f.write("1;Article A;-5\n")

        with open("ligne_incomplete.csv", "w", encoding="utf-8") as f:
            f.write("1;Article A\n")

    def tearDown(self):
        for fname in ["valid.csv", "prix_text.csv", "prix_negatif.csv", "ligne_incomplete.csv"]:
            os.remove(fname)

    def test_csv_valide(self):
        result = charger_csv("valid.csv")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["nom"], "Article A")
        self.assertEqual(result[2]["prix"], 5.75)

    def test_fichier_absent(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("absent.csv")

    def test_prix_non_numerique(self):
        with self.assertRaises(LigneInvalideException):
            charger_csv("prix_text.csv")

    def test_prix_negatif(self):
        with self.assertRaises(PrixNegatifException):
            charger_csv("prix_negatif.csv")

    def test_ligne_incomplete(self):
        with self.assertRaises(LigneInvalideException):
            charger_csv("ligne_incomplete.csv")

if __name__ == "__main__":
    unittest.main()
