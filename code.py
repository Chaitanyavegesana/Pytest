#f = open("input.txt", "r")
#for x in f:
 # print(x)
import re
filename = "SBLAYOUT.txt"
outputstring =''


def DataType(clause):
	if 'X' in clause:
		if 'XX' in clause or '(' in clause :
			return 'String'
		return 'Integer'
	elif 'Z' in clause:
		return 'decimal'
	
for line in open(filename, 'r'):

	if "PIC" in line:
		k = re.sub(' +', ' ',line)
		li = list(k.split(" ")) 
		datatype = DataType(li[4])
		outputstring = outputstring + li[2] + ':' + datatype + '|'
print(outputstring)
	
