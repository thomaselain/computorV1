from term import Term, LEFT, RIGHT
from error import errors_search
from process import process
import sys
import re

arg = "".join(sys.argv[1].split()) 

# Ca, mec, c'est beau (tres beau) (et satrouv un coef avec d truc de ouf genre des / ou des - ou des . ou tout a la fois (c fou))
# [0-9]+(?:[\.][+-]?[0-9]+)?(?:\/[-+]?[0-9]+(?:[\.][0-9]+)?)?

regex = re.compile('([+-]*[0-9\.]+\/*[0-9\.]*)(?:\*?([Xx](?:\^([0-9]+))?))?')
is_valid = re.compile('^([+-]*(?:[0-9]+(?:[\.][0-9]+)?(?:\/[0-9]+(?:[\.][0-9]+)?)?\*?[xX]\^[0-9]+|[0-9]+\*?[xX]|[xX]|[0-9]+))+=([+-]*(?:[0-9]+\*?[xX]\^[0-9]+|[0-9]+\*?[xX]|[xX]|[0-9]+))+$')

errors_search()

# if len(is_valid.findall(arg)) == 0:
# 	print("ntm c pa bon")
# 	exit()

left = regex.findall(arg[:arg.find('=')])
right = regex.findall(arg[arg.find('='):])
Terms = list()

for current in left:
	Terms.append(Term(current, LEFT))
for current in right:
	Terms.append(Term(current, RIGHT))

for term in Terms:
	term.debug()

process(Terms)