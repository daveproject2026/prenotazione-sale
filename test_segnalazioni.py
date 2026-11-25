import unittest
from datetime import date

from prenotazioni import Prenotazione


class TestSegnalazioni(unittest.TestCase):
    def test_prenotazioni_contigue(self):
        giorno = date(2026, 11, 24)

        prima = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 5)
        seconda = Prenotazione("A2", giorno, "10:00", "11:00", "Bianchi", 5)

        self.assertFalse(prima.si_sovrappone(seconda))


if __name__ == "__main__":
    unittest.main()
