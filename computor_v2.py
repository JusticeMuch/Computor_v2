class Func:

    a = b = c = sol1 = sol2 = 0
    discriminant = False

    def __init__(self, str):
        self.str = str.split(" ")
        self.a = self.b = self.c = float(0)
        for k in range(0,len(self.str)):
            if "X^" in self.str[k]:
                tempCoef = int(self.str[k].replace("X^",""))
                hpd = hpd if hpd > tempCoef else tempCoef
                if (hpd > 2 or tempCoef < 0):
                    print("The degree of this function is not within the range of 0 and 2")
                    exit()
                elif ("*" in self.str[k]  and k != 1):
                    t = float(self.str[k - 2])
                    t = (t * -1)if k > 2 and "-" in self.str[k - 3] else t
                    t = (t * -1)if k > 2 and "=" in self.str[k - 4] else t
                    t = (t * -1)if k > 2 and "=" in self.str[k - 3] else t
                    if tempCoef == 0:
                        self.c += t
                    elif tempCoef == 1:
                        self.b += t    
                    elif tempCoef == 2:
                        self.a += t
    
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
        self.sol1 = self.sol2 = 0
        if (self.a != 0 ):
            sq = (self.b * self.b) - 4*self.a*self.c
            self.discriminant =  False if (sq < 0) else True
            if (self.discriminant == True):
                self.sol1 = (-(self.b) + self.sqrt(sq))/ (2 * self.a)
                self.sol2 = (-(self.b) - self.sqrt(sq))/ (2 * self.a)
            elif (self.b != 0):
                self.sol1 = -1 * (self.c / self.b)
    
    def FunctionCall(self, val):
        return self.a * val * val + self.b * val + self.c

class Matrices:

    columns = rows = 0
    matrix = []

    def __init__ (self, inp):
        self.matrix.append([])
        if type(inp) is list:
            self.matrix = inp
        else:
            self.strSplit = inp.split(" ")
            self.strSplit = self.strSplit[2]
            self.strSplit = self.strSplit.split[";"]
            self.columns = len(self.strSplit)
            self.rows = len(self.strSplit[0].split(","))
            for i in range (0, len(self.strSplit)):
                self.strSplit[i] =self.strSplit[i].replace("[", "")
                self.strSplit[i] =self.strSplit[i].replace("]", "")
                temp =self.strSplit[i].split(",")
                if (len(temp) != self.rows):
                    print ("Error, the number or rows is not equivalent for each column ")
                    exit()
                for k in range (0, len(temp)):
                    self.matrix[i][k] = int(temp[k])

    def add(self, matrix2):
        result = []
        result.append([])
        if (self.columns != matrix2.columns):
            print("The matrices cannot be added as the sizes don't match")
            exit()
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                result[i][j] = self.matrix[i][j] + matrix2.matrix[i][j]
        return Matrices(result)

    def subtract(self, matrix2):
        result = []
        result.append([])
        if (self.columns != matrix2.columns):
            print("The matrices cannot be added as the sizes don't match")
            exit()
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                result[i][j] = self.matrix[i][j] - matrix2.matrix[i][j]
        return Matrices(result)

    def multiply(self, matrix2):
        result = []
        result.append([])
        if (self.columns != matrix2.rows):
            print("The columns are not equivalent to the rows of the other matrix")
            exit()
        for i in range (0, self.rows):
            for j in range (0, matrix2.columns):
                result[i][j] = 0
                for k in range (0, self.columns):
                    result += (self.matrix[i][k] * matrix2.matrix[k][j])
        return Matrices(result) 

class ComplexNumbers:

    imag = real = 0

    # def __init__(self, inpStr):
    #     self.strSplit = inpStr.split(" ")
    #     self.imag = int(self.strSplit[2].replace("i", "")) if "i" in self.strSplit[2] else int(self.strSplit[4].replace("i", ""))
    #     self.real = int(self.strSplit[2]) if "i" not in self.strSplit[2] else int(self.strSplit[4])

    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def multply(self,compNum2):
        real = (self.real * compNum2.real) + (-1)*(self.imag * compNum2.imag)
        imag = (self.real * compNum2.imag) + (compNum2.real * self.imag)
        return ComplexNumbers(real, imag)

    def add (self, compNum2):
        return ComplexNumbers(self.real + compNum2.real , self.imag + compNum2.imag)

    def subtract (self, compNum2):
        return ComplexNumbers(self.real + compNum2.real , self.imag + compNum2.imag)

    