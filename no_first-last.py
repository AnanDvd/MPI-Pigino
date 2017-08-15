'''
15-08-2017

MPI-CBG, Pigino Lab

Using the replicated file, in which each line was
duplicated twice, this script deletes one duplication
each from the first line and the last line. Keeps the
header intact. The output is written in a new file, in
which the MOTL from the original file is replaces with REPLICATE
'''


import pathlib

#Make sure that the script is placed
#in the same directory, and the current
#directory is the working directory
path = pathlib.Path('.')

#Just to check if the directory is valid or not
assert path.is_dir(), "{} is not a valid directory".format(file_name.absolute())


#Operates on all .csv files in the current directory
for file_name in path.glob('*.csv'):

    #Opens the file in read mode
    with file_name.open('r') as fi:

        #Opens a new file in write mode
        with pathlib.Path(str(file_name).replace('MOTL', 'REPLICATE')).open('w') as fo:

            #Prints header
            fo.write("CCC;reserved;reserved;pIndex;wedgeWT;NA;NA;NA;NA;NA;xOffset;yOffset;zOffset;NA;NA;reserved;EulerZ(1);EulerZ(3);EulerX(2);reserved;CREATED WITH PEET Version 1.9.1 04/01/2014")
            fo.write("\n")

            #Skips second and last line of the file
            #because the first line is the header
            for line in list(fi)[2:-1]:
                fo.write(line)
