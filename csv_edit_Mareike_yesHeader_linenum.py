import fileinput

with fileinput.input(inplace=True) as f:

    for linenum, line in enumerate(f):
        if linenum == 0:
            continue
        
        n = 1

        line = line.rstrip('\n')
        numbers = line.split(sep = ',')

        for i in range(3):
            numbers[3] = n
            n += 1
            s = ''
            for i in numbers:
                s += str(i) + ','
            s = s.rstrip(',')
            print(s)
    
        
