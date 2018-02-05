"""
This code receives an argument from a PHP code (could be any code really though.  Since a sentence is received as an array it appends
the array together to get one string called result.

It is important to note that the Website will grab the first print statement it sees and return that to the user.
THERE SHOULD BE ONLY ONE PRINT STATEMENT IN THE FINAL VERSION OR THIS WILL NOT WORK, the print statement acts as a return statement.
"""

import sys

args = sys.argv[1:]#grabs the arguments (user's query)
result = ""

for arg in args: #Loops through the arguments (User's query) to convert it from an array to a string since arguments are passed as an array
	result += (arg + " ")
	
result += ("here is an added on sentence")#appends an new line to the query
print (result)#returns the query to the user