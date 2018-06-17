from reduce import reduce
from term import Term, LEFT, RIGHT
import sys

def process(term_array):
	a = 0
	b = 0
	c = 0
	for term in term_array:
	    if term.expo < 0 or term.expo > 2:
	        print ("ComputorV1 only handles polynomials of degree 2 or less\n")
	        exit()
	    if term.side == RIGHT:
	        term.invert()
	    if term.expo == 2:
	        a += term.coef * term.sign
	    elif term.expo == 1:
	        b += term.coef * term.sign
	    elif term.expo == 0:
	        c += term.coef * term.sign

	delta = b ** 2 - 4 * (a * c)

	reduced = reduce({\
			"a" : Term(-1 if a < 0 else 1, a, 2),\
			"b" : Term(-1 if b < 0 else 1, b, 1),\
			"c" : Term(-1 if c < 0 else 1, c, 0)\
		})
	print("\nReduced form is : " + reduced)

	if a == 0:
		if reduced.find('x') == -1:
			print("\nThis equation is nonsense, you need an X to solve one !")
			exit()
		elif b == 0:
			print("\nOh... no solution, probably because you forgot the 'X' (stopping now)")
			exit()
		print("\nThis equation is of degree 1")
		res_one = -c / (2 * b)
		print('''One real root
	X = ''' + str(res_one))
	else:
		print("\nThis equation is of degree 2")
		print("Delta is " + str(delta) + "\n")
		if delta > 0:
		    res_one = (-b + (delta ** 0.5)) / (2 * a)
		    res_two = (-b - (delta ** 0.5)) / (2 * a)
		    print ('''Positive --> two real roots
	X1 = ''' + str(res_one) + '''
	X2 = ''' + str(res_two) + '\n')
		elif delta == 0:
		    res_one = - (b / (2 * a))
		    print (''' --> one real root\n
	X = ''' + str(res_one) + '\n')
		elif delta < 0:
			fraction_len = len(str(-delta)) + len(str(-b) if b != 0 else "") + 5
			i = 0

	# First solution
			print('Negative --> two complex roots\n')

			sys.stdout.write("     " + (str(-b) + " "  if b != 0 else "") +  "- iV(" + str(-delta) + ")\nZ1 = ")
			while i <= fraction_len:
				sys.stdout.write('-')
				i += 1
			i = 0
			sys.stdout.write("\n")
			while i <= fraction_len / 2 - len(str(-2 * a)) + 6:
				sys.stdout.write(' ')
				i += 1
			print(str(-2 * a) + "\n")
	# Second solution
			i = 0
			sys.stdout.write("     " + (str(-b) + " "  if b != 0 else "") +  "+ iV(" + str(-delta) + ")\nZ2 = ")
			while i <= fraction_len:
				sys.stdout.write('-')
				i += 1
			i = 0
			sys.stdout.write("\n")
			while i <= fraction_len / 2 - len(str(-2 * a)) + 6:
				sys.stdout.write(' ')
				i += 1
			print(str(-2 * a))