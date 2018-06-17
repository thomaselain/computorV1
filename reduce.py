def reduce(term_array):
	res = ""
	if term_array["a"].coef != 0:
		res += ("" if term_array["a"].sign == 1 else "-") + str(abs(term_array["a"].coef)) + "x^2 "
	if term_array["b"].coef != 0:
		res += ("" if term_array["a"].coef == 0 else "+ " if term_array["b"].sign == 1 else "- ") + str(abs(term_array["b"].coef)) + "x "
	if term_array["c"].coef != 0:
		res += ("" if term_array["a"].coef == 0 and term_array["b"].coef == 0 else "+ " if term_array["c"].sign == 1 else "- ") + str(abs(term_array["c"].coef)) + " "
	return res + "= 0"
