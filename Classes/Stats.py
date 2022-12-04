class Stats:
    def __init__(self):
        self.stats={
            "BULLS":0,
            "COWS":0
        }

    def zwieksz_Bulls(self):
        self.stats["BULLS"]=self.stats["BULLS"]+1

    def zwieksz_Cows(self):
        self.stats["COWS"]=self.stats["COWS"]+1

    def zeruj_staty(self):
        self.stats["BULLS"]=0
        self.stats["COWS"]=0