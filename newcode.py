#f = open("input.txt", "r")
#for x in f:
 # print(x)
import re
filename = "SBLAYOUT.TXT"
outputstring =''


def DataType(clause):
	if 'X' in clause and '(' in clause :
		getva = clause.replace('X','')
		getvb = getva.rstrip('.')
		return 'char' + getvb
	elif 'X' in clause:
		countx = str(clause.count('X'))
		
		return 'char(' + countx + ')'
	elif 'Z' in clause or 'S' in clause or 'V' in clause:
		return 'decimal(10,4)'
	else:
		return 'String'
	
	
for line in open(filename, 'r'):

	if "PIC" in line:
		commentline = line
		if ' *' not in commentline:
			final = commentline
#			print(final)
			k = re.sub(' +', ' ',final)
			li = list(k.split(" "))
#			print(li[4])
			datatype = DataType(li[4])
			outputstring = outputstring + li[2] + ':' + datatype + '|'
print(outputstring)
		