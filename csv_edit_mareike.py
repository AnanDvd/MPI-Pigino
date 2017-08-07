'''
07-08-2017

Pigino Lab, MPI-CBG

Edits the csv file, doubling the x,y,z values, and
removing the first line (header). No semi-colon issue
because Mareike has the updated csv reader

'''

import fileinput
import sys
import codecs

with fileinput.input(inplace=True) as f:
    with fileinput.input(inplace=True) as f1:

        #Skips the first line in the csv file
        next(f)
        for line in f:

           
            line = line.rstrip('\n');
            

            #array that stores the index value of all the semicolons in the line
            sc_pos_array = [i for i,x in enumerate(line) if x == ',']
            
            #Multiplies and replaces x,y,z values by 2* the value 
            line = line[0:sc_pos_array[9]+1] + str(2 * float(line[sc_pos_array[9]+1 : sc_pos_array[10]])) + "," + str(2 * float(line[sc_pos_array[10]+1 : sc_pos_array[11]])) + "," + str(2 * float(line[sc_pos_array[11]+1 : sc_pos_array[12]])) + line[sc_pos_array[12]:]     
            

            print(line)
        
