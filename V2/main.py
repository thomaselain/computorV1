from term import Term, LEFT, RIGHT
from error import errors_search
import sys
import re

regex = re.compile('=?([+-]*[0-9]+[\.\/ ]*[0-9]*)(?:\*?([Xx](?:\^([0-9]+))?))?')
errors_search()

arg = sys.argv[1]

left = regex.findall(arg[:arg.find('=')])
right = regex.findall(arg[arg.find('='):])
Terms = list()

for current in left:
	Terms.append(Term(current, LEFT))
for current in right:
	Terms.append(Term(current, RIGHT))

for term in Terms:
	term.debug()
