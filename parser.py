#!/usr/bin/env python3

# Script to parse a maillog file and output to STDOUT in tab delimited
# format IP, Username and date
# maintained by rodatwork@gmail.com
# python version 3.8.10

import sys
import re

scriptname = "parser.py"

def usage():
    print("Please supply a filename or pipe maillog_test to script")
    print("Usage: ' cat maillog_test |", scriptname,"> outputfile.txt ' OR")
    print("'",scriptname, "maillog_test > outputfile.txt '")

#function that does the brunt of the work. Parses the data stream
def parse(data):
        # Look for lines that have AUTH= in them
        authline = re.search(r'^.*AUTH=(.*.)\s$', data)
        # select lines with AUTH= and ignore ones that don't
        if authline:                                    
            # Take the month & correct the case of corrupted month i.e. "aalJul"
            regex = re.compile("^.*(Jul|Aug|Sep|Oct|Nov|Dec|Jan|Feb|Mar|Apr|May|Jun)\s"
            # Get Date, IP and Username
            "(\d+)\s.*.\[(\d+\.\d+\.\d+\.\d+)\].*.authid=(.*.),\smech")                
            result = regex.match(data)
            # Print result order: IP, Username, Month, Date. Tab separated
            print(result.group(3),result.group(4),result.group(1),result.group(2), sep = '\t' )

# Determine how we are being called. By Filename? By Pipe?
if sys.stdin.isatty():    
    try:
        filename = (sys.argv[1])
        # If we get an IndexError we know the program has
        # been called without a filename   
    except IndexError:
        usage()
        exit()
        # If we are here an argument has been supplied, but is it a filename?
    try:
        input = open(filename, 'r') 
        for line in input: #line = file.read()
            # send data stream to parse() function to perform regex
            # and output to StdOut
            parse(line)
    except FileNotFoundError:
        print("Supplied argument is not a filename. Please enter a valid")
        print("filename like '",scriptname," maillog_test > outputfile.txt '")
    except NameError:
        usage()
        exit()
else:
    # script is being called by pipe
    for line in sys.stdin:
        # send data stream to parse() function to perform regex
        # and output to StdOut
        parse(line)

