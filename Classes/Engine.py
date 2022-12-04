from Dictionary import Dictionary
from Validator import Validator
from Stats import Stats
import random as rand
v1=Validator()
d=Dictionary()

class Engine(Dictionary):
    res = Stats()
    czworka=0
    trojka=0
    licznik_prob=10

    def __init__(self):
        super().__init__()

    def gra(self,user,cpu):
        self.res.zeruj_staty()
        b1=[char for char in cpu]
        b2=[char for char in user]
        for i in range(len(b1)):
            if b1[i] == b2[i]:
                self.res.zwieksz_Bulls()
            else:
                for j in range(len(b2)):
                    if b1[i] == b2[j]:
                        self.res.zwieksz_Cows()
        return self.res

    def zasady_gry(self):
        return "Zasady gry:\n\nTekstowa gra w ktorej komputer (Host) losuje slowo, ktore jest izogramem (izogram jest to wyraz,\n"\
               "w ktorym nie powtarzaja sie zadne litery) i informuje uzytkownika (Guesser) o ilosci liter w slowie.\n"\
               "Uzytkownik (Guesser) stara sie zgadnac co to za slowo Komputer (Host) po kazdej probie zwraca liczbe Cows & Bulls.\n"\
               "Liczba przy slowie Cows oznacza litere wystepujaca w slowie lecz na zlej pozycji, liczba przy slowie Bulls oznacza poprawna litere na poprawnej pozycji.\n"\
               "Gra konczy sie kiedy liczba przy Bulls bedzie taka sama jak dlugosc slowa wylosowanego przez komputer.\n\n"

    def eksport_wyniku(self,wynik):
        print("Czy chcesz wyeksportowac swoj wynik do pliku tekstowego?\nT-TAK\nN-NIE")
        op1 = input("Twoj wybor: ")
        if op1.upper() == "T":
            with open("highscore.txt", "a") as f:
                B, C = wynik.stats['BULLS'], wynik.stats['COWS']
                f.write(f"BULLS: {B}, COWS: {C}\n")

    def dodawanie_do_bazy(self):
        passwd = "haslo123"
        passwd_user = input("Ta opcja jest zarezerwowana dla adminow, aby kontynuowac podaj haslo: ")
        if passwd_user == passwd:
            new = input("Podaj haslo ktore chcesz dodac do bazy danych: ")
            if v1.check(new):
                print(d.dodaj_w_baze(new))
            else:
                print("Twoje slowo nie jest izogramem!!!\n")
        else:
            print("Bledne haslo!!!\n")

    def zmien_trudnosc(self):
        x=input("Podaj dlugosc hasla ktore chcesz odgadnac: ")
        tmp=0
        for s in self.baza_danych:
            if len(s)!=int(x):
                tmp=tmp+1
        if tmp==len(self.baza_danych):
            print("Brak w bazie slow o takiej dlugosci!!!\n")
            self.czworka=0
        else:
            y=[words for words in self.baza_danych if len(words)==int(x)]
            self.czworka=1
            return rand.choice(y)

    def zmien_proby(self):
        x = input("Podaj ile chcesz miec prob: ")
        self.trojka=1
        return x

    def powrot_do_pierwotnej_trudnosci(self):
        t = input("\nCzy chcesz wrocic do pierwotnego poziomu trudnosci?\nT-TAK\nN-Nie\nTwoj wybor: ")
        if t.upper() == "T":
            self.czworka=0


    def powrot_do_pierwotnej_ilosci_prob(self):
        r = input("\nCzy chcesz aby licznik prob ponownie wynosil 10?\nT-TAK\nN-Nie\nTwoj wybor: ")
        if r.upper() == "T":
            self.licznik_prob=10
            self.trojka=0

    def menu(self):
        print("Wybierz jedna z opcji: \n")
        print("1.Nowa gra\n2.Zasady gry\n3.Zmien liczbe prob\n4.Wybierz poziom trudnosci\n5.Dodaj nowa propozycje do bazy danych\n6.Wyswietl baze danych z haslami\n7.Koniec\n")
        return int(input("Twoj wybor: "))

    def user_input(self,d1):
        print(f"Komputer wylosowal slowo o dlugosci {len(d1)}\nLiczba dostepnych prob: {self.licznik_prob}\n")
        user=input("Sprobuj odgadnac slowo przeciwnika!!!\nJezeli chcesz przerwac i wrocic do menu wpisz: \"KONIEC\"\nTwoj wybor: ").upper()
        if user=="KONIEC":
            return 0
        else:
            if len(user)!=len(d1):
                return 0
            else:
                if v1.check(user):
                    return user
                else:
                    return False

    def wybory_uzytkownika(self):
        if self.czworka == 1:
            self.powrot_do_pierwotnej_trudnosci()
        if self.trojka == 1:
            self.powrot_do_pierwotnej_ilosci_prob()

    def sprawdz_wygrana(self,d1):
        if self.res.stats["BULLS"] == len(d1):
            print("Wygrales gratuluje!!!\n")
            self.wybory_uzytkownika()
            return 1
        else:
            return 0

    def wyswietlanie_bazy(self):
        w=input("Czy jestes pewny, ta opcja moze zepsuc ci zabawe?\nT-TAK\nN-Nie\nTwoj wybor: ")
        if w.upper() == "T":
            print("\n")
            print("\n".join(self.baza_danych))
            print("\n")
