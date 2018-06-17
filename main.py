import sys
from process import process
from term import Term, LEFT, RIGHT

# computor_input = "5 * X^1 + -4 * X^1 + +9.3 * X^2 = 1 * X^0"

if len(sys.argv) == 1:
    print("\nOops, looks like you forgot the equation")
    exit()
elif len(sys.argv) > 2:
    print("\nPlease give me equations one by one")
    exit()
elif sys.argv[1].count('=') == 0:
    print("\nHey, an equation needs a '=' to work")
    exit()
elif sys.argv[1].count('=') > 1:
    print("\nThere are too many '=', slow down !")
    exit()


computor_input = sys.argv[1]

term_array = []
side = LEFT
i = 0

jump = computor_input.find('X', 0, computor_input.find('='))
if jump == -1:
    i = computor_input.find('=')

# Parsing block -> stores a b and c on both sides in term_array
while i < len(computor_input):
    sign = -1 if computor_input[i] == '-' else 1
    if (computor_input[i] == '-' or computor_input[i] == '+'):
        i += 1
    if (computor_input[i] == '='):
        if computor_input.find('X', i) == -1:
            break
        side = RIGHT
        i += 1
    current_term = Term(sign)
    coefpos = computor_input.find('*', i)
    current_term.set_coef(float(computor_input[i:coefpos]))
    i = computor_input.find('* X^', i) + 4
    expopos = computor_input.find(' ', i)
    if (expopos == -1):
        current_term.set_expo(int(computor_input[i:]))
    else:
        current_term.set_expo(int(computor_input[i:expopos]))
    i = computor_input.find(
        ' ', i) + 1 if expopos != -1 else i + 1
    current_term.set_side(side)
    term_array.append(current_term)
# for term in term_array:
#     term.debug()
#     print("\n\n")

process(term_array)