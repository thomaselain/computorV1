LEFT  =  1
RIGHT = -1
# indexes for values[]
SIGN   =  0
NUM    =  1
EXP    =  2
import re

class Term():
    def __init__(self, values, side = LEFT):
        slash = str(values[NUM]).find('/')

        if values[NUM] != '':
            sign = 1 if str(values[SIGN]).count('-') % 2 == 0 else -1

            if slash == -1:
                self.num = float(str(values[NUM]).replace('-', '')) * sign
            else:
                self.num = float(values[NUM][:slash]) * sign / float(values[NUM][slash + 1:])
            if values[EXP] == '':
                self.expo = 0
            elif str(values[EXP]).lower() == 'x':
                self.expo = 1
            elif str(values[EXP]).find('^') != -1:
                self.expo = int(values[EXP][str(values[EXP]).find('^') + 1:])
        else:
            self.num = 1 if str(values[SIGN]).count('-') % 2 == 0 else -1
            if values[EXP] == '':
                self.expo = 0
            elif str(values[EXP]).lower() == 'x':
                self.expo = 1
            elif str(values[EXP]).find('^') != -1:
                self.expo = int(values[EXP][str(values[EXP]).find('^') + 1:])

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
        self.num *= -1
        self.side *= -1

    def exists(self):
        return self.num != 0

    def get_sign(self):
        if (self.exists()):
            return "-" if self.num < 0 else "+"
        else:
            return ""