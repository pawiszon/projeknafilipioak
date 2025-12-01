from system_rezerwacji import SystemRezerwacji
from wydarzenie import Wydarzenie

def main():
    system = SystemRezerwacji()
    plik = "wydarzenia.txt"

    while True:
        print("=== System rezerwacji biletów ===")
        print("1. Dodaj wydarzenie")
        print("2. Rezerwuj miejsca")
        print("3. Anuluj rezerwację")
        print("4. Wyświetl wydarzenia")
        print("5. Zapisz do pliku")
        print("6. Wczytaj z pliku")
        print("0. Wyjdź")
        wybor = input("Wybór: ")
        print()

        if wybor == "1":
            nazwa = input("Podaj nazwę: ")
            data = input("Podaj datę: ")
            try:
                miejsca = int(input("Podaj liczbę miejsc: "))
            except:
                print("Błędna liczba miejsc!\n")
                continue

            system.dodaj_wydarzenie(Wydarzenie(nazwa, data, miejsca))

        elif wybor == "2":
            nazwa = input("Podaj nazwę wydarzenia: ")
            w = system.znajdz(nazwa)
            if not w:
                print("Nie znaleziono wydarzenia.\n")
                continue

            try:
                liczba = int(input("Ile miejsc zarezerwować? "))
            except:
                print("Błędna liczba!\n")
                continue

            if w.rezerwuj(liczba):
                print("Zarezerwowano.\n")
            else:
                print("Brak wystarczającej liczby miejsc.\n")

        elif wybor == "3":
            nazwa = input("Podaj nazwę wydarzenia: ")
            w = system.znajdz(nazwa)
            if not w:
                print("Nie znaleziono wydarzenia.\n")
                continue

            try:
                liczba = int(input("Ile miejsc anulować? "))
            except:
                print("Błędna liczba!\n")
                continue

            if w.anuluj(liczba):
                print("Anulowano.\n")
            else:
                print("Nie można anulować więcej miejsc niż zarezerwowano.\n")

        elif wybor == "4":
            system.wyswietl_wydarzenia()

        elif wybor == "5":
            system.zapisz_do_pliku(plik)

        elif wybor == "6":
            system.wczytaj_z_pliku(plik)

        elif wybor == "0":
            print("Zakończono program.")
            break

        else:
            print("Nieznana opcja.\n")


if __name__ == "__main__":
    main()




//SYSTEM_REZERWACJI.PY



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



//WYDARZENIE.PY 




class Wydarzenie:
    def __init__(self, nazwa, data, liczba_miejsc):
        self.nazwa = nazwa
        self.data = data
        self.liczba_miejsc = liczba_miejsc
        self.zarezerwowane = 0

    def rezerwuj(self, liczba):
        if self.zarezerwowane + liczba > self.liczba_miejsc:
            return False
        self.zarezerwowane += liczba
        return True

    def anuluj(self, liczba):
        if liczba > self.zarezerwowane:
            return False
        self.zarezerwowane -= liczba
        return True

    def wolne_miejsca(self):
        return self.liczba_miejsc - self.zarezerwowane

    def __str__(self):
        return (f"Nazwa: {self.nazwa}, Data: {self.data}, Miejsca: {self.liczba_miejsc}, "
                f"Zarezerwowane: {self.zarezerwowane}, Wolne: {self.wolne_miejsca()}")

    def to_file_string(self):
        return f"{self.nazwa};{self.data};{self.liczba_miejsc};{self.zarezerwowane}"

    @staticmethod
    def from_file_string(line):
        parts = line.strip().split(";")
        if len(parts) != 4:
            return None
        w = Wydarzenie(parts[0], parts[1], int(parts[2]))
        w.zarezerwowane = int(parts[3])
        return w