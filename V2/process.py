from term import Term, LEFT, RIGHT
import sys

def get_degree(Terms):
	if Terms[2].exists():
		return 2
	elif Terms[1].exists():
		return 1
	else:
		return 0

def print_complex(Terms, delta):
	if not (len(sys.argv) == 3 and sys.argv[1] == "-f"):
		sys.stdout.write("\n\tz1 = ")
		if round(Terms[1].num / (2 * Terms[2].num), 3) != 0:
			sys.stdout.write(str(round(Terms[1].num / (2 * Terms[2].num), 3)))
		sys.stdout.write((" + " if (abs(delta) / (2 * Terms[2].num) > 0) else " - ") + str(round(abs(delta) / (2 * Terms[2].num),3)) + "i\n" )
		sys.stdout.write("\n\tz2 = ")
		if round(Terms[1].num / (2 * Terms[2].num), 3) != 0:
			sys.stdout.write(str(round(Terms[1].num / (2 * Terms[2].num), 3)))
		sys.stdout.write((" + " if (-abs(delta) / (2 * Terms[2].num) > 0) else " - ") + str(round(abs(delta) / (2 * Terms[2].num),3)) + "i\n" )
		return
	up_z1 = (str(Terms[1].num) + " +" if Terms[1].num != 0 else "") + " i * sqrt(" + str(abs(delta)) + ")"
	up_z2 = (str(Terms[1].num) if Terms[1].num != 0 else "") + " - i * sqrt(" + str(abs(delta)) + ")"
	if (2 * Terms[2].num == 1): # on n'affiche le trait du milieu que si le denominateur (a) = 1
		print("\nz1 = " + up_z1 + "\n\nz2 = " + up_z2)
		return
	else:
		print("\n")
		print_soluce(Terms, up_z1, 1)
		print("\n")
		print_soluce(Terms, up_z2, 2)

def print_soluce(Terms, up, z):
	x=0
	sys.stdout.write("\t" + up + "\nz" + str(z) + " =\t")
	while x < len(up):
		sys.stdout.write("-")
		x+=1
	sys.stdout.write("\n\t")
	x=0
	while x < len(up) / 2 - len(str(2*Terms[2].num)) / 2:
		sys.stdout.write(" ")
		x+=1
	print(str(2 * Terms[2].num))




def process(Terms):
	reduced = [Term(["", 0, 0]), Term(["", 0, 1]), Term(["", 0, 2])]

	for term in Terms:
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
		res += ("" if reduced[2].num >= 0 else "-") + str(abs(reduced[2].num)) + "x^2 "
	if reduced[1].exists():
		res += ("" if reduced[2].num == 0 else "+ " if reduced[1].num >= 0 else "- ") + str(abs(reduced[1].num)) + "x^1 "
	if reduced[0].exists():
		res += ("" if reduced[2].num == 0 and reduced[1].num == 0 else "+ " if reduced[0].num >= 0 else "- ") + str(abs(reduced[0].num)) + " "
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
		print("One real root : \n\tx = " + str(-reduced[0].num / reduced[1].num))
	if (degree == 2):
		delta = reduced[1].num ** 2 - 4 * reduced[2].num * reduced[0].num
		if delta > 0:
			print("Delta = " + str(delta) + ", wich is > 0, so there are two real roots :")
			print("\n\tx1 = " + str((-reduced[1].num + delta ** 0.5) / (2 * reduced[2].num)))
			print("\n\tx2 = " + str((-reduced[1].num - delta ** 0.5) / (2 * reduced[2].num)))
		elif delta == 0:
			print("Delta = " + str(delta) + ", so there is one real root :")
			print("\tx = " + str(-reduced[1].num / (2 * reduced[2].num)))
		elif delta < 0:
			print("Delta = " + str(delta) + ", wich is < 0, so there are two complex roots :")
			print_complex(reduced, delta)
