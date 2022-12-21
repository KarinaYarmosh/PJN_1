import re

def main():
    file = open("plik.csv", "r")
    for row in file:
        if re.match(r"[a-zA-Z]+;\d+;\d+", row):
            print("Poprawna linia")
        else:
            print("Niepoprawna linia")

if __name__ == '__main__':
    main()
