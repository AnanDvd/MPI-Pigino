'''
31-07-2017

Pigino Lab, MPI-CBG

Edits the csv file, doubling the x,y,z values,
deletes last semicolon from each line, and then replaces
all the semicolons with comma
'''

import fileinput
import sys
import codecs
import os

with fileinput.input(inplace=True) as f:
    with fileinput.input(inplace=True) as f1:

        
            #Skips the first line in the csv file
            next(f)

            print("CCC;reserved;reserved;pIndex;wedgeWT;NA;NA;NA;NA;NA;xOffset;yOffset;zOffset;NA;NA;reserved;EulerZ(1);EulerZ(3);EulerX(2);reserved;CREATED WITH PEET Version 1.9.1 04/01/2014")
            for line in f:

                #removes ; from the end of all lines where it appears
                #leaves all other lines unchanged
                line = line.rstrip('\n');
                #if line.endswith(';'):
                #line = line[:-1]

                #array that stores the index value of all the semicolons in the line
                sc_pos_array = [i for i,x in enumerate(line) if x == ',']
                
                #Multiplies and replaces x,y,z values by 2* the value 
                line = line[0:sc_pos_array[9]+1] + str(2 * float(line[sc_pos_array[9]+1 : sc_pos_array[10]])) + "," + str(2 * float(line[sc_pos_array[10]+1 : sc_pos_array[11]])) + "," + str(2 * float(line[sc_pos_array[11]+1 : sc_pos_array[12]])) + line[sc_pos_array[12]:]

                #finally, replace all the semicolons with comma
                #line = line.replace(';',',')      
                

                print(line)

        
        
