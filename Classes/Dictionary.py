import random as rand


class Dictionary:
    def __init__(self):
        try:
            with open("dictionary.txt","r") as f:
                self.baza_danych=[x for x in f.read().split('\n')]
        except FileNotFoundError:
            print("Brak pliku")

    def dodaj_w_baze(self,str):
        try:
            with open("dictionary.txt","a") as f1:
                for word in self.baza_danych:
                    if word==str.upper():
                        return "To haslo jest juz w bazie!!!\n"
                f1.write("\n"+(str.upper()))
                self.baza_danych.append(str.upper())
                return "Dodano twoje haslo do bazy!!!\n"
        except FileNotFoundError:
            print("Brak pliku")

    def random(self):
        return rand.choice(self.baza_danych)



