import tempfile
import sys

with open('testdrive_copy_marieke.csv', 'r') as file:
    num_of_lines = file.read().count('\n')
    #print(num_of_lines)
    file.seek(0)
    i = 0
    with open('new.csv', 'w')as newfile:
        for line in file:
            if i != 1 and i != num_of_lines-1:
                newfile.write(line)
            i = i+1
