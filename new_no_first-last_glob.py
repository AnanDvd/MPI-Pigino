import pathlib


path = pathlib.Path('.')

assert path.is_dir(), "{} is not a valid directory".format(file_name.absolute())

for file_name in path.glob('*.csv'):
    #print(path.is_dir())
    
    with file_name.open('r') as fi:
        with pathlib.Path(str(file_name).replace('test', 'xyz')).open('w') as fo:
            fo.write("CCC;reserved;reserved;pIndex;wedgeWT;NA;NA;NA;NA;NA;xOffset;yOffset;zOffset;NA;NA;reserved;EulerZ(1);EulerZ(3);EulerX(2);reserved;CREATED WITH PEET Version 1.9.1 04/01/2014")
            
            for line in list(fi)[2:-1]:
                fo.write(line)
