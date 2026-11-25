import unittest
from datetime import date, timedelta

from prenotazioni import (
    Agenda,
    DataNonAmmessa,
    Prenotazione,
    PrenotazioneNonTrovata,
    Sala,
    SalaNonTrovata,
)


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.sala = Sala("A2", "Sala riunioni", 10)
        self.agenda.aggiungi_sala(self.sala)
        self.oggi = date(2026, 11, 24)

    def test_sala_duplicata(self):
        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(self.sala)

    def test_sala_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("X99")

    def test_data_passata(self):
        giorno = self.oggi - timedelta(days=1)
        prenotazione = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 5)

        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(prenotazione, oggi=self.oggi)

    def test_domenica(self):
        giorno = date(2026, 11, 29)
        prenotazione = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 5)

        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(prenotazione, oggi=self.oggi)

    def test_data_oltre_orizzonte(self):
        giorno = self.oggi + timedelta(days=61)
        prenotazione = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 5)

        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(prenotazione, oggi=self.oggi)

    def test_prenotazione_oggi(self):
        prenotazione = Prenotazione("A2", self.oggi, "09:00", "10:00", "Rossi", 5)

        identificativo = self.agenda.prenota(prenotazione, oggi=self.oggi)

        self.assertEqual(identificativo, 1)

    def test_cancella_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(999)

    def test_prenotazione_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(999)


if __name__ == "__main__":
    unittest.main()
