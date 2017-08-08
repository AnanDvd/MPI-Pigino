import fileinput

with fileinput.input(inplace=True) as f:
    iterF = iter(f)
    next(iterF)

    n = 1
    for line in iterF:
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
        
