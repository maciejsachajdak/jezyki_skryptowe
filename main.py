from Dictionary import Dictionary
from Validator import Validator
from Engine import Engine
print("Witaj w grze \"Bulls and Cows\"\n")
v1=Validator()
e1=Engine()
d=Dictionary()
op=0
while op!=7:
    op=e1.menu()
    if op==1:
        if e1.czworka == 1:
            d1 = e
        else:
            d1 = d.random()
        while e1.licznik_prob > 0:
            us=e1.user_input(d1)
            if us==0:
                e1.licznik_prob=0
            else:
                user=us
                if isinstance(user,int) and user>1:
                    print(f"Podaj slowo dlugosci {len(d1)}!!! Twoje slowo ma dlugosc {user}\n")
                elif user!=False and isinstance(user,str):
                    wynik = e1.gra(user, d1)
                    print(wynik.stats)
                    e1.eksport_wyniku(wynik)
                    if e1.sprawdz_wygrana(d1)==1:
                        break
                    else:
                        e1.licznik_prob = e1.licznik_prob - 1
                else:
                    print("Twoje slowo nie jest izogramem!!!\n")


        if e1.licznik_prob == 0:
            print("Przegrales :((((")
            e1.licznik_prob=10
            e1.wybory_uzytkownika()

    elif op==2:
        print(e1.zasady_gry())
    elif op==3:
        e1.licznik_prob=int(e1.zmien_proby())
    elif op==4:
        e=e1.zmien_trudnosc()
    elif op==5:
        e1.dodawanie_do_bazy()
    elif op==6:
        e1.wyswietlanie_bazy()
    elif op>7:
        print("Brak takiej opcji!")

