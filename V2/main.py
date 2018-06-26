#!/usr/bin/python3
from term import Term, LEFT, RIGHT
from process import process
import sys
import re

if len(sys.argv) == 3:
	if sys.argv[1] == "-f":
		arg = "".join(sys.argv[2].split())
	else:
		print("invalid parameter\nUsage : ./computorV1 [-f] \"equation\"")
		exit()
else:
	arg = "".join(sys.argv[1].split()) 


# Problemes :
#	Ca oublie certains signes au debut des affichages de la forme reduite

# Ca, mec, c'est beau (tres beau) (et satrouv un coef avec d truc de ouf genre des / ou des - ou des . ou tout a la fois (c fou))
# [0-9]+(?:[\.][+-]?[0-9]+)?(?:\/[-+]?[0-9]+(?:[\.][0-9]+)?)?

one_term_regex = r"(?:([-+]*\d+(?:\.\d+)?(?:\/[+-]*\d+(?:\.\d+)?)?)(\*?[xX](?:\^[0-2])?)?)|(?:([+-]*[xX](?:\^[0-2])?))"
regex = re.compile(one_term_regex)
is_valid = re.compile('^(' + one_term_regex + ")+=(" + one_term_regex + ")+$")

if len(is_valid.findall(arg)) == 0:
	print("ntm c pa bon")
	exit()

left = regex.findall(arg[:arg.find('=')])
right = regex.findall(arg[arg.find('='):])
Terms = list()

for current in left:
	print(current)
	Terms.append(Term(current, LEFT))
for current in right:
	print(current)
	Terms.append(Term(current, RIGHT))
		
process(Terms)