class Func:

    a = b = c = sol1 = sol2 = 0
    discriminant = False

    def __init__(self, str):
        self.str = str.split(" ")
        Func.a = Func.b = Func.c = float(0)
        for st in str:
            if "X^" in st:
                tempCoef = int(st.replace("X^",""))
                i = str.index(st)
                hpd = hpd if hpd > tempCoef else tempCoef
                if (hpd > 2 or tempCoef < 0):
                    break
                elif ("*" in st  and i != 1):
                    t = float(str[i - 2])
                    t = (t * -1)if i > 2 and "-" in str[i - 3] else t
                    t = (t * -1)if i > 2 and "=" in str[i - 4] else t
                    t = (t * -1)if i > 2 and "=" in str[i - 3] else t
                    if tempCoef == 0:
                        Func.c += t
                    elif tempCoef == 1:
                        Func.b += t    
                    elif tempCoef == 2:
                        Func.a += t
    
    def sqrt(self, x):
        if (x == 0 or x == 1):
            return x
        i = 0.001
        result = 1
        while (result <= x): 
            i += 0.001
            result = i * i
        return i

    def solve(self):
        Func.sol1 = Func.sol2 = 0
        if (Func.a != 0 ):
            sq = (Func.b * Func.b) - 4*Func.a*Func.c
            Func.discriminant =  False if (sq < 0) else True
            if (Func.discriminant == True):
                Func.sol1 = (-(Func.b) + Func.sqrt(self, sq))/ (2 * Func.a)
                Func.sol2 = (-(Func.b) - Func.sqrt(self, sq))/ (2 * Func.a)
            elif (Func.b != 0):
                Func.sol1 = -1 * (Func.c / Func.b)

class Matrices:

    columns = rows = 0
    matrix = []

    def __init__ (self, inpString):
        self.strSplit = inpString.split(" ")
        self.strSplit = self.strSplit[2]
        
        
