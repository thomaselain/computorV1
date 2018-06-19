from term import Term, LEFT, RIGHT
import sys

def get_degree(Terms):
	if Terms[2].exists():
		return 2
	elif Terms[1].exists():
		return 1
	else:
		return 0

def process(Terms):
	print("\nProcess started\n-----------\n")
	reduced = [Term([0, "", 0], 0), Term([0, "", 1]), Term([0, "", 2])]

	for term in Terms:
		if term.side == RIGHT:
			term.change_side()
		if (int(term.expo) <= 2):
			reduced[int(term.expo)].num += float(term.num)
		else:
			print("This program can only handle equations of 2nd degree or lower")
			exit()
	# for term in reduced:
	# 	term.debug()

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
	sys.stdout.write("Reduced form : ")
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
			print("Delta = " + str(delta) + ", wich is < 0, so there are two imaginary roots :")
