from term import Term, LEFT, RIGHT
from error import errors_search
from process import process
import sys
import re

regex = re.compile('([+-]*[0-9\.]+\/*[0-9\.]*)(?:\*?([Xx](?:\^([0-9]+))?))?')
reg_term = "(?:([-+]*\d+(?:\.\d+)?(?:\/[+-]*\d+(?:\.\d+)?)?)(\*?[xX](?:\^[0-2])?)?)|(?:([+-]+)?([xX](?:\^[0-2])?))"
is_valid = re.compile("^("+reg_term+")+=("+reg_term+")+$")
arg = "".join(sys.argv[1].split()) if len(sys.argv) > 1 else 'No parameter'
print(is_valid.findall(arg))

term_regex = re.compile(reg_term)
left = term_regex.findall(arg[:arg.find('=')])
right = term_regex.findall(arg[arg.find('='):])

errors_search()

if len(is_valid.findall(arg)) == 0:
	print("ntm c pa bon")
	exit()
else:
	print("coucou c bon")

Terms = list()

for term in left:
	print(term)
for term in right:
	print(term)

for current in left:
	Terms.append(Term(current, LEFT))
for current in right:
	Terms.append(Term(current, RIGHT))

for term in Terms:
	term.debug()

process(Terms)