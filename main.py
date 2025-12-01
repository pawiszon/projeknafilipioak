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



