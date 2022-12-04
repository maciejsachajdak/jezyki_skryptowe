import pytest
from Engine import Engine
@pytest.fixture
def engine():
    return Engine()

def test_res(engine):
    wynik=engine.gra("abc","bac")
    assert wynik.stats["BULLS"]==1 and wynik.stats["COWS"]==2

def test_sprawdz_wygrana(engine):
    engine.gra("abc","abc")
    assert engine.sprawdz_wygrana("abc")==1

def test_sprawdz_przegrana(engine):
    engine.gra("abc","qwe")
    assert engine.sprawdz_wygrana("qwe")==0

