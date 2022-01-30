import argparse
import glob
import os
import sys
import statistics


def show_statistics(file_name, filter_syntax):
    values = []
    with open(file_name) as f:
        lines = f.readlines()[1:]
        nr_of_args = 2
        try:
            date, temp = lines[0].strip().split(',')
        except ValueError:
            date, temp, humidity = lines[0].strip().split(',')
            nr_of_args = 3

        for line in lines:
            if nr_of_args == 2:
                date, temp = line.strip().split(',')
            else:
                try:
                    date, temp, humidity = line.strip().split(',')
                except ValueError:
                    print(f'ValueError={line}')
            if filter_syntax:
                if date.startswith(filter_syntax):
                    values.append(float(temp))
            else:
                values.append(float(temp))

    print(f'Filename {file_name}')
    print(f'Nr of samples {len(values)}')
    if len(values) > 0:
        print(f'min {min(values)}')
        print(f'max {max(values)}')
        print(f'mean {statistics.mean(values)}')
        print(f'median {statistics.median(values)}')

        return (len(values), min(values), max(values), statistics.mean(values), statistics.median(values))
    else:
        return (0, 0, 0, 0, 0)


def main():
    my_parser = argparse.ArgumentParser(description='Read temperature from csv file')

    # Add the arguments
    my_parser.add_argument('Files',
                           nargs='+',
                           metavar='files',
                           type=str,
                           help='data file to read')

    my_parser.add_argument('-f',
                           '--filter',
    #                      action='store_true',
                           type=str,
                           help='simple filtering, implemented as str.startswith(filter), for example use filter 2021-12 for showing data for december in 2021',
                           required=False)

    args = my_parser.parse_args()
    # args, unknown = my_parser.parse_known_args()
    
    file_names = args.Files
    filter_syntax = args.filter
    if filter_syntax and filter_syntax != '':
        print('Filter: {}'.format(filter_syntax))

    
    if file_names[0].startswith('*'):
        file_list = glob.glob(file_names[0])
        file_names = file_list

    for file_name in file_names:
        if not os.path.isfile(file_name):
            print(f'The file {file_name} does not exist')
            sys.exit()

    for file_name in file_names:
        show_statistics(file_name, filter_syntax)
        print()


if __name__ == "__main__":
    main()
