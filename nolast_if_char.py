'''
31-07-2017

Pigino Lab, MPI-CBG

This script deletes the last character from all the lines that
end with a semicolon. Lines that don't end with a semicolon will
remain unchanged. To modify in order to delete last character if
it is somethig else, please see the comment in the script, before the
if statement.
'''

import fileinput

with fileinput.input(inplace=True) as f:
    for line in f:
        line = line.rstrip('\n');

        '''
        Within the single quotes insdie the brackets, we can
        replace the ; with any other character we want, that we
        want to delete from all the lines. 
        '''
        if line.endswith(';'):
            line = line[:-1]
            
        print (line)
