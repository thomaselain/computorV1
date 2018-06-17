LEFT = 0
RIGHT = 1
class Term():
    def __init__(self, sign=1, coef=0, expo=0, side=LEFT):
        self.coef = coef
        self.expo = expo
        self.sign = sign
        self.side = side

    def set_sign(self, sign):
        self.sign = sign
    
    def set_coef(self, coef):
        self.coef = coef

    def set_expo(self, expo):
        self.expo = expo

    def set_side(self, side):
        self.side = side
        
    def debug(self):
        print(
            "coef = " + str(self.coef)
            + "\nsign = " + str(self.sign)
            + "\nexpo = " + str(self.expo)
            + "\nside = " + str(self.side))
    def invert(self):
        self.sign *= -1