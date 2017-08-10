'''
07-08-2018

MPI-CBG, Pigino Lab

Replicates each line in the csv file thrice, and
updates the pIndex (4th value in the line). For the
moment, if we want to copy the lines 'n' number of times,
please replace the '3' in the <for i in range(3)> line with 'n'
'''


import fileinput

with fileinput.input(inplace=True) as f:
    with fileinput.input(inplace=True) as f1:
        next(f)

        n = 1

        #Print header
        print("CCC;reserved;reserved;pIndex;wedgeWT;NA;NA;NA;NA;NA;xOffset;yOffset;zOffset;NA;NA;reserved;EulerZ(1);EulerZ(3);EulerX(2);reserved;CREATED WITH PEET Version 1.9.1 04/01/2014")
        for line in f:
            line = line.rstrip('\n')

            #Separates the values in the line by every comma
            numbers = line.split(sep=',')

            #If we want to copy each line 3 times
            #Replace 3 with the number of how many times
            #you want to copy the lines
            for i in range(3):

                #The pIndex is at the 4th position in the line
                #Counting in array starts from 0, hence 3
                numbers[3] = n
                n += 1    #Increases the pIndex
                s = ''
                for i in numbers:
                    s += str(i) + ','  #Adds back the commas
                s = s.rstrip(',')    #Removes the comma from the end of line

                
                print(s)
                

            

