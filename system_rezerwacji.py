import os
from wydarzenie import Wydarzenie

class SystemRezerwacji:
    def __init__(self):
        self.wydarzenia = []

    def dodaj_wydarzenie(self, wydarzenie):
        self.wydarzenia.append(wydarzenie)
        print("Dodano wydarzenie.")

    def wyswietl_wydarzenia(self):
        if not self.wydarzenia:
            print("Brak wydarzeń.")
            return

        print("\n--- Lista wydarzeń ---")
        for w in self.wydarzenia:
            print(w)
        print("-----------------------\n")

    def znajdz(self, nazwa):
        for w in self.wydarzenia:
            if w.nazwa.lower() == nazwa.lower():
                return w
        return None

    def zapisz_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, "w", encoding="utf-8") as f:
            for w in self.wydarzenia:
                f.write(w.to_file_string() + "\n")
        print("Zapisano do pliku.")

    def wczytaj_z_pliku(self, nazwa_pliku):
        if not os.path.exists(nazwa_pliku):
            print("Plik nie istnieje.")
            return

        self.wydarzenia.clear()
        with open(nazwa_pliku, "r", encoding="utf-8") as f:
            for line in f:
                w = Wydarzenie.from_file_string(line)
                if w:
                    self.wydarzenia.append(w)

        print("Wczytano wydarzenia z pliku.")