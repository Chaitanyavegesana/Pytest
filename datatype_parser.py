"""TODO: 
"""
from __future__ import print_function  # Python 2/3 compatibility

import json
import logging


"""
Datatype_parser reads the file from S3 or folder location and parse the file for filed name and converts the COBOL datatype to DynamoDB datatypes . 
Stores the Datatype in DEV-life_it-sourcemasterlist dynamodb table as record . 
"""

import re



def DataType(clause):
	if 'X' in clause:
		if 'XX' in clause or '(' in clause :
			return 'String'
		return 'Integer'
	elif 'Z' in clause:
		return 'decimal'

def parser_handler(filename):
	outputstring =''
	for line in open(filename, 'r'):
		if "PIC" in line:
			trim = re.sub(' +', ' ', line)
			listing = list(trim.split(" ")) 
			datatype = DataType(listing[4])
			outputstring = outputstring + listing[2] + ':' + datatype + '|'
	return outputstring


def lambda_handler(event, context):
	file_key = event['file_key']
	response = parser_handler(file_key)
	print(response) 
      
            

        