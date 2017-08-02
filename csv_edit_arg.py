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
import argparse
import sys


ap = argparse.ArgumentParser()
ap.add_argument("-m", "--multiplier", required = True, help = "number to multiply with x,y,z values")
args = vars(ap.parse_args())


#a = int(sys.argv[1])

with fileinput.input(inplace=True) as f:
    with fileinput.input(inplace=True) as f1:

        #Skips the first line in the csv file
        next(f)
        for line in f:

            #removes ; from the end of all lines where it appears
            #leaves all other lines unchanged
            line = line.rstrip('\n');
            if line.endswith(';'):
                line = line[:-1]

            #array that stores the index value of all the semicolons in the line
            sc_pos_array = [i for i,x in enumerate(line) if x == ';']
            
            #Multiplies and replaces x,y,z values by 2* the value 
            line = line[0:sc_pos_array[9]+1] + str(args["multiplier"] * float(line[sc_pos_array[9]+1 : sc_pos_array[10]])) + ";" + str(args["multiplier"] * float(line[sc_pos_array[10]+1 : sc_pos_array[11]])) + ";" + str(args["multiplier"] * float(line[sc_pos_array[11]+1 : sc_pos_array[12]])) + line[sc_pos_array[12]:]

            #finally, replace all the semicolons with comma
            line = line.replace(';',',')      
            

            print(line)
            
