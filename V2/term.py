LEFT  =  1
RIGHT = -1
NUM   =  0
X     =  1
EXP   =  2
class Term():
    def __init__(self, values, side):
        slash = str(values[NUM]).find('/')
        if slash != -1:
            values[NUM].replace(' ', '')
            self.num = float(values[NUM][:slash]) / float(values[NUM][slash + 1:])
        else:
            self.num = values[NUM]

        if values[EXP] != "":
            self.expo = values[EXP]
        elif values[X] == "":
            self.expo = 0
        else:
            self.expo = 1

        self.side = side

    def set_coef(self, num):
        self.num = num

    def set_expo(self, expo):
        self.expo = expo

    def set_side(self, side):
        self.side = side
        
    def debug(self):
        print(
            "num = " + str(self.num)
            + "\nexpo = " + str(self.expo)
            + "\nside = " + ("LEFT" if self.side == LEFT else "RIGHT") + "\n")
    def change_side(self):
        self.side *= -1