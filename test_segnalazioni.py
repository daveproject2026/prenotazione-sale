import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def test_prenotazioni_contigue(self):
        giorno = date(2026, 11, 24)

        prima = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 5)
        seconda = Prenotazione("A2", giorno, "10:00", "11:00", "Bianchi", 5)

        self.assertFalse(prima.si_sovrappone(seconda))

    def test_capienza_esatta(self):
        giorno = date(2026, 11, 24)
        agenda = Agenda()
        sala = Sala("A2", "Sala riunioni", 10)
        agenda.aggiungi_sala(sala)

        prenotazione = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 10)

        identificativo = agenda.prenota(prenotazione, oggi=giorno)

        self.assertEqual(identificativo, 1)


if __name__ == "__main__":
    unittest.main()
