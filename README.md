# System rezerwacji biletów
## Opis
Projekt działa tak że rezerwuje bilety napisany w języku pajton

## Wymagane biblioteki: 
1. json
2. os

## Jak uruchomić?
w konsoli
```
python3 main.py
```
## Opis klas
* Wydarzenie - ma nazwę licze miejsc i funkcje do rezerwacji i anulacji
* System rezerwacji - dodawanie wydarzeń, wyświetlanie, znajduwanie, zapisywanie do pliku i czytywanie z pliku

## klasa wydarzenie: 
parametry nazwa, data, liczba miejsc, liczba zarezerwowanych

### Najważniejsze funkcje w tej klasie:
1. rezeruj - przyjmuje parametr liczba
2. Anuluj - przyjmjące paramet liczba
## Klasa Program: 
Główna klasa programu

### Najważniejsze funkcje w tej klasie:
1. pokaż menu - pokazuje menu
2. DOdaj wydarzenie - uruchamia skrypt dodawania wydawrzenia
3. wyświetl wydarzenie - uruchamia skrypt wyświetlania wydarzenie
4. rezerwuj bilety - rezerwuje bilety
5. anuluj rezerwacje - uruchamia skrypt do anulowania rezerwacji

## Autor: Paweł Maśka, 01.12.2025 
