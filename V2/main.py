from term import Term, LEFT, RIGHT
from error import errors_search
from process import process
import sys
import re

arg = "".join(sys.argv[1].split()) 

# Problemes :
# 	- (term) Ca marche pas et ca comprend ca commme 0 * (terme)
#	Ca oublie certains signes au début des affichages de la forme réduite


# Ca, mec, c'est beau (tres beau) (et satrouv un coef avec d truc de ouf genre des / ou des - ou des . ou tout a la fois (c fou))
# [0-9]+(?:[\.][+-]?[0-9]+)?(?:\/[-+]?[0-9]+(?:[\.][0-9]+)?)?
one_term_regex = "(?:([-+]+)?(\d+(?:\.\d+)?(?:\/[+-]*\d+(?:\.\d+)?)?)(\*?[xX](?:\^[0-2])?)?)|(?:([+-]+)?([xX](?:\^[0-2])?))"
regex = re.compile(one_term_regex)
is_valid = re.compile('^(' + one_term_regex + ")+=(" + one_term_regex + ")+$")

errors_search()

if len(is_valid.findall(arg)) == 0:
	print("ntm c pa bon")
	exit()

left = regex.findall(arg[:arg.find('=')])
right = regex.findall(arg[arg.find('='):])
Terms = list()

for current in left:
	if current[0] or current[1] or current[2]:
		Terms.append(Term(current, LEFT))
for current in right:
	if current[0] or current[1] or current[2]:
		Terms.append(Term(current, RIGHT))
		
process(Terms)