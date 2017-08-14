import fileinput
import numpy as np

with fileinput.input(inplace=True) as f:
    with fileinput.input(inplace=True) as f1:
        next(f)

        n = 0
        
        print("CCC;reserved;reserved;pIndex;wedgeWT;NA;NA;NA;NA;NA;xOffset;yOffset;zOffset;NA;NA;reserved;EulerZ(1);EulerZ(3);EulerX(2);reserved;CREATED WITH PEET Version 1.9.1 04/01/2014")
        for line in f:
            line = line.rstrip('\n')
            #cnt = sum(1 for line in f if line.rstrip('\n'))
            #linenum = len(list(f))
                    
            numbers = line.split(sep=',')

            for i in range(3):
                
                numbers[3] = n
               
                n += 1
                s = ''
                for i in numbers:
                    s += str(i) + ','
                s = s.rstrip(',')

                
                result = []
                result.append(s)
                result = result[1:-1]
                print(result)

                
