#!/usr/bin/python3
from term import Term, LEFT, RIGHT
from process import process
import sys
import re

reg_term = r"(?:([-+]*)(\d+(?:\.\d+)?(?:\/[+-]*\d+(?:\.\d+)?)?)(\*?[xX](?:\^[0-9]+)?)?)|(?:([+-]*)([xX](?:\^[0-9]+)?))"
is_valid = re.compile('^(' + reg_term + ")+=(" + reg_term + ')+$')
if len(sys.argv) == 3:
	if sys.argv[1] == "-f":
		arg = "".join(sys.argv[2].split())
	else:
		print("Invalid parameter\nUsage : ./computorV1 [-f] \"equation\"")
		exit()
elif len(sys.argv) == 1:
    print("No parameters, Exiting...")
    exit()
else:
    arg = "".join(sys.argv[1].split())

term_regex = re.compile(reg_term)
left = term_regex.findall(arg[:arg.find('=')])
right = term_regex.findall(arg[arg.find('='):])

if len(is_valid.findall(arg)) == 0:
    print('Regex did not pass, please try again with this type of format : \n\t./computorV1 "ax^2 + bx + c = ..."\n\t./computorV1 "a * x^2 + b * x^1 + c * x^0 = ..."\n(a, b, c, "*", " ", "^1", and "x^0" are optionnal)')
    exit()

terms = list()

for term_index in range(len(left)):
    if (term_index != 0 and left[term_index][0] == '' and left[term_index][3] == ''):
        print("Missing sign before term: " + left[term_index][0] +left[term_index][1] +left[term_index][2] +left[term_index][3] +left[term_index][4])
        exit()
    terms.append(Term(left[term_index], LEFT))
for term_index in range(len(right)):
    if (term_index != 0 and right[term_index][0] == '' and right[term_index][3] == ''):
        print("Missing sign before term: " + right[term_index][0] +right[term_index][1] +right[term_index][2] +right[term_index][3] +right[term_index][4])
        exit()
    terms.append(Term(right[term_index], RIGHT))

process(terms)
