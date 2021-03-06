from term import Term, LEFT, RIGHT
import sys


def get_degree(terms):
    if terms[2].exists():
        return 2
    elif terms[1].exists():
        return 1
    else:
        return 0


def print_complex(terms, delta):
    if len(sys.argv) != 3 and sys.argv[1] != "-f":
        sys.stdout.write("\tz1 = ")
        z1= (-terms[1].num - delta ** 0.5) / (terms[2].num * 2)
        print("{:g}".format(round(z1.real, 2) + round(z1.imag, 2) * 1j))
        sys.stdout.write("\n\tz2 = ")
        z2 = (-terms[1].num + (delta ** 0.5)) / (terms[2].num * 2)
        print("{:g}".format(round(z2.real, 2) + round(z2.imag, 2) * 1j))
        return
    up_z1 = (str(round(terms[1].num, 3)) + " +" if terms[1].num !=
             0 else "") + " i * sqrt(" + str(round(abs(delta), 3)) + ")"
    up_z2 = (str(round(terms[1].num, 3)) if terms[1].num != 0 else "") + \
        " - i * sqrt(" + str(round(abs(delta), 3)) + ")"
    if (2 * terms[2].num == 1):  # on n'affiche le trait du milieu que si le denominateur (a) = 1
        print("\nz1 = " + up_z1 + "\n\nz2 = " + up_z2)
        return
    else:
        print("\n")
        print_soluce(terms, up_z1, 1)
        print("\n")
        print_soluce(terms, up_z2, 2)


def print_soluce(terms, up, z):
    x = 0
    sys.stdout.write("\t" + up + "\nz" + str(z) + " =\t")
    while x < len(up):
        sys.stdout.write("-")
        x += 1
    sys.stdout.write("\n\t")
    x = 0
    while x < len(up) / 2 - len(str(2*terms[2].num)) / 2:
        sys.stdout.write(" ")
        x += 1
    print(str(2 * terms[2].num))


def process(terms):
    reduced = [Term(["", "0", 'x^2', '', ''], LEFT), Term(
        ["", '0', "x", '', ''], LEFT), Term(["", '0', '', '', ''], LEFT)]

    for term in terms:
        if term.side == RIGHT:
            term.change_side()
        if (int(term.expo) <= 2):
            reduced[int(term.expo)].num += float(term.num)
        else:
            print("This program can only handle equations of 2nd degree or lower")
            exit()

    # Printing the reduced form
    res = ""

    if reduced[2].exists():
        res += str(reduced[2].num) + "x^2 "
    if reduced[1].exists():
        if reduced[2].exists():
            res += "+ " if reduced[1].num >= 0 else "- "
            res += str(abs(reduced[1].num)) + "x "
        else:
            res += str(reduced[1].num) + "x "
    if reduced[0].exists():
        if reduced[2].exists() or reduced[1].exists():
            res += "+ " if reduced[0].num >= 0 else "- "
            res += str(abs(reduced[0].num)) + " "
        else:
            res += str(reduced[0].num) + " "

    if not reduced[2].exists() and not reduced[1].exists() and not reduced[0].exists():
        res += "0 "
    sys.stdout.write("\nReduced form : ")
    print(res + "= 0")
    # End of printing

    degree = get_degree(reduced)

    print("\nThis equation is of degree " + str(int(degree)) + "\n")
    if (degree == 0):
        if (reduced[0].num == 0):
            print("All real numbers are solutions of this equation")
        else:
            print("No solution for this equation")
        exit()
    if (degree == 1):
        print("One real root : \n\tx = " +
              str(-reduced[0].num / reduced[1].num))
    if (degree == 2):
        delta = reduced[1].num ** 2 - 4 * reduced[2].num * reduced[0].num
        if delta > 0:
            print("Delta = " + str(delta) +
                  ", wich is > 0, so there are two real roots :")
            print("\n\tx1 = " +
                  str((-reduced[1].num + delta ** 0.5) / (2 * reduced[2].num)))
            print("\n\tx2 = " +
                  str((-reduced[1].num - delta ** 0.5) / (2 * reduced[2].num)))
        elif delta == 0:
            print("Delta = " + str(delta) + ", so there is one real root :")
            print("\tx = " + str(-reduced[1].num / (2 * reduced[2].num)))
        elif delta < 0:
            print("Delta = " + str(delta) +
                  ", wich is < 0, so there are two complex roots :")
            print_complex(reduced, delta)
