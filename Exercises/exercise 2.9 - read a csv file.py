import os
import sys

filename = '../Sandbox/ca-500.csvX'

# Look before you leap
if not os.path.isfile(filename):
    print(f'File {filename} not found.')
    sys.exit(-1)

# Easier to ask for forgiveness than permission
try:
    with open(filename, mode='r') as f:

        headers = f.readline().strip().split(';')

        for line in f:
            values = line.strip().split(';')

            d = dict(zip(headers, values))

            if d['city'] in ('Montreal', ):
                print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")

except FileNotFoundError:
    print(f'File {filename} not found.')





# import csv
#
# with open(filename, 'r') as f:
#     reader = csv.DictReader(f, delimiter=';')
#
#     for d in reader:
#
#         if d['city'] in ('Montreal', 'Toronto'):
#             print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")
