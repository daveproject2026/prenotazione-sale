import unittest
from datetime import date

from prenotazioni import Prenotazione


class TestPrenotazione(unittest.TestCase):
    def setUp(self):
        self.giorno = date(2026, 11, 24)

    def test_orari_non_ammessi(self):
        casi = [
            ("09:15", "10:00"),
            ("07:30", "09:00"),
            ("19:00", "20:30"),
            ("10:00", "10:00"),
            ("10:00", "09:00"),
        ]

        for inizio, fine in casi:
            with self.subTest(inizio=inizio, fine=fine):
                with self.assertRaises(ValueError):
                    Prenotazione("A2", self.giorno, inizio, fine, "Rossi", 5)

    def test_giorno_tipo_errato(self):
        with self.assertRaises(TypeError):
            Prenotazione("A2", "2026-11-24", "09:00", "10:00", "Rossi", 5)

    def test_durata_minuti(self):
        prenotazione = Prenotazione("A2", self.giorno, "09:00", "10:30", "Rossi", 5)

        self.assertEqual(prenotazione.durata_minuti(), 90)


if __name__ == "__main__":
    unittest.main()
