import re
import unidecode

def read_file(path):
    with open(path, "r", encoding='utf-8') as file:
        data = file.read()
        file.close()
    return data

def uni(text):
    unaccented_string = unidecode.unidecode(text)
    #print(unaccented_string)
    return unaccented_string

def find_kurw(text):
    pattern = '[A-Za-z0-9]*[kq][uo0]?r[e]?w[A-Za-z0-9]+'
    kurwa = re.sub(pattern, '*****', text)
    return kurwa

def find_jeb(text):
    pattern2 = '[A-Za-z0-9]*jeb[A-Za-z0-9]+'
    jebac = re.sub(pattern2, '*****', text)
    return jebac

def find_pierd(text):
    pattern3 = '[A-Za-z0-9]*pierd[A-Za-z0-9]+'
    pierdolec = re.sub(pattern3, '*****', text)
    return pierdolec

def find_pieprz(text):
    pattern3 = '[A-Za-z0-9]*pieprz[A-Za-z0-9]+'
    pieprz = re.sub(pattern3, '*****', text)
    return pieprz

def find_sra(text):
    pattern4 = '[A-Za-z0-9]*sr[ay][A-Za-z0-9]+'
    sra = re.sub(pattern4, '*****', text)
    return sra

def find_pizd(text):
    pattern5 = '[A-Za-z0-9]*pizd[A-Za-z0-9]+'
    pizd = re.sub(pattern5, '*****', text)
    return pizd

def find_dup(text):
    pattern6 = '[A-Za-z0-9]*dup[A-Za-z0-9]+'
    dup = re.sub(pattern6, '*****', text)
    return dup

def find_suk(text):
    pattern7 = '[A-Za-z0-9]*suk[A-Za-z0-9]+'
    suk = re.sub(pattern7, '*****', text)
    return suk

def find_chu(text):
    pattern8 = '[A-Za-z0-9]*huj[A-Za-z0-9]+'
    chuj = re.sub(pattern8, '*****', text)
    return chuj

def find_cip(text):
    pattern9 = '[A-Za-z0-9]*cip[A-Za-z0-9]+'
    cip = re.sub(pattern9, '*****', text)
    return cip

def find_kut(text):
    pattern10 = '[A-Za-z0-9]*kutas*[A-Za-z0-9]+'
    kutas = re.sub(pattern10, '*****', text)
    return kutas

with open("../../../../Desktop/p/pythonProject1/PJN/PJN2/end_file.csv", "w", encoding='utf-16') as file:
    file.write(find_kut(find_chu(find_cip(find_suk(find_dup(find_pizd(find_sra(find_pieprz(find_pierd(find_jeb(find_kurw(uni(read_file(
        "../../../../Desktop/p/pythonProject1/PJN/PJN2/plik2.csv"))))))))))))))
    file.close()
