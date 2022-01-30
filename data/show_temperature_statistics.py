import argparse
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

    print(f'min {min(values)}')
    print(f'max {max(values)}')
    print(f'mean {statistics.mean(values)}')
    print(f'median {statistics.median(values)}')


def main():
    my_parser = argparse.ArgumentParser(description='Read temperature from csv file')

    # Add the arguments
    my_parser.add_argument('File',
                           metavar='file',
                           type=str,
                           help='data file to read')

    my_parser.add_argument('-f',
                           '--filter',
    #                      action='store_true',
                           type=str,
                           help='simple filtering, implemented as str.startswith(filter), for example use filter 2021-12 for showing data for december in 2021',
                           required=False)

    my_parser.add_argument("-n", "--name", help="your name")

    # Execute the parse_args() method
    args = my_parser.parse_args()

    file_name = args.File
    filter_syntax = args.filter
    if filter_syntax:
        print('Filter: {}'.format(filter_syntax))

    name = args.name
    if name:
        print('Name: {}'.format(name))

    if not os.path.isfile(file_name):
        print(f'The file {file_name} does not exist')
        sys.exit()
        
    show_statistics(file_name, filter_syntax)


if __name__ == "__main__":
    main()
