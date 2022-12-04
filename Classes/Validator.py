class Validator:

    def check(self,str):
        ml=str.lower()
        d=0
        for char in ml:
            if ml.count(char)>1:
                d=d+1
        if d>1:
            return False
        else:
            return True