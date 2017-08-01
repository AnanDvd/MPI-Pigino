'''
28-07-2107

Pigino Lab, MPI-CBG

This is a general script that deletes the last character
from every line, no matter what the character is.

Note: the script modifies the original file.
'''


import fileinput

with fileinput.input(inplace=True) as f:
    for line in f:
        line = line.rstrip('\n');
        line = line[:-1]

        print(line)
