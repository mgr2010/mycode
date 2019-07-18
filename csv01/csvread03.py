import csv
import argparse

parser = argparse.ArgumentParser(description="CSV File name")
parser.add_argument('-f', type=str, help="csv file name", required=True)
cmdargs = parser.parse_args()
csv_file = cmdargs.f

with open(csv_file, mode='w') as csv_file:
    fieldnames = ['hostname', 'ip', 'service']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'})
    writer.writerow({'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'})
