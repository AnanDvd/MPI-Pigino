import pathlib

path = pathlib.Path('~/MPI-Pigino')
for file_name in path.glob('*.csv'):
    print(path.is_dir())
    with open(file_name, 'r') as fi:
        with open(file_name.replace('csv', 'out'), 'w') as fo:
            for line in list(fi)[1:-1]:
                fo.write(line)
