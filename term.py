LEFT = 1
RIGHT = -1
# indexes for values[]
NUM_SIGN = 0
NUM = 1
NUM_EXPO = 2
X_SIGN = 3
X = 4

import re


class Term():
    def __init__(self, term_dict, side):
        self.num = term_dict[NUM] if term_dict[NUM] != '' else 1
        self.expo = term_dict[NUM_EXPO] if term_dict[NUM_EXPO] != '' else term_dict[X] if term_dict[X] != '' else '0'
        sign = 1
        if (term_dict[NUM_SIGN]):
            sign = 1 if str(term_dict[NUM_SIGN]).count('-') % 2 == 0 else -1
        elif(term_dict[X_SIGN]):
            sign = 1 if str(term_dict[X_SIGN]).count('-') % 2 == 0 else -1        
        slash = str(self.num).find('/')
        self.num = float(self.num[:slash]) / float(self.num[slash + 1:]) if slash != -1 else self.num
        if (self.expo.find('^') != -1):
            self.expo = int(self.expo[self.expo.find('^') + 1:]) if self.expo.find('^') != -1 else self.expo
        self.expo = '1' if str(self.expo).lower().find('x') != -1 else self.expo
        self.side = side
        self.num = float(self.num) * sign

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
