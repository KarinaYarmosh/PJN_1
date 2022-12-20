import re

def main():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    telefon = input("Podaj telefon: ")
    kod_pocztowy = input("Podaj kod pocztowy: ")
    miasto = input("Podaj miasto: ")

    if imie[0].isupper() and nazwisko[0].isupper() and miasto[0].isupper():
        print("Imie, nazwisko i miasto zaczynaja sie wielka litera")
    else:
        print("Imie, nazwisko i miasto nie zaczynaja sie wielka litera")

    if re.match(r"\(\d{2}\)\s\d{3}-\d{2}-\d{2}", telefon):
        print("Telefon jest w formacie: (61) 222-45-56")
    else:
        print("Telefon nie jest w formacie: (61) 222-45-56")

    if re.match(r"\d{2}-\d{3}", kod_pocztowy):
        print("Kod pocztowy jest w formacie: 11-111")
    else:
        print("Kod pocztowy nie jest w formacie: 11-111")

if __name__ == '__main__':
    main()


