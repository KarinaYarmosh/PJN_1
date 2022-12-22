import re

def main():
    with open("../../../../Desktop/p/pythonProject1/PJN/PJN2/plik3.csv", "r") as file:
        data = file.read()
        file.close()
    file2 = open("../../../../Desktop/p/pythonProject1/PJN/PJN2/plik4.csv", "w")
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.+[a-zA-Z0-9-.]+', data)
    for email in emails:
        print(email)
        file2.write(email + " ")


if __name__ == '__main__':
    main()