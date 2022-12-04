from Stats import Stats
import pytest

@pytest.fixture
def punkty():
    return Stats()

def test_dodaj_Bullls(punkty):
    punkty.zwieksz_Bulls()
    punkty.zwieksz_Bulls()
    assert punkty.stats["BULLS"]==2

def test_dodaj_Cows(punkty):
    punkty.zwieksz_Cows()
    assert punkty.stats["COWS"]==1

def test_zeruj(punkty):
    punkty.zwieksz_Bulls()
    punkty.zwieksz_Bulls()
    punkty.zwieksz_Cows()
    punkty.zeruj_staty()
    assert punkty.stats["COWS"]==0 and punkty.stats["BULLS"]==0