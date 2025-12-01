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