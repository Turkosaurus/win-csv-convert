import os
import csv

'''
Removes Byte Order Marker (BOM) from begginning of UTF-8 CSVs in source path
Recreates ASCII CSV in destination path
'''

# Path Variables
current_path = os.getcwd()
print(f"current_path: {current_path}")

tmp_path = current_path + "\\tmp\\"
source_path = tmp_path + "input\\"
print(f"source_path: {source_path}")

dest_path = tmp_path + "output\\"
print(f"dest_path: {dest_path}")

# File list
filelist = os.listdir(source_path)
print(f"filelist: {filelist}")

print("-" * 80)

# Loop source_path for files
for file in filelist:

    if file.endswith(".csv"):
        print(f"Converting {file}...")

        # Open and read current CSV
        with open(source_path + file, 'r') as f:
            csv_reader = csv.reader(f)

            # Read CSV into list
            data = []
            for line in csv_reader:
                data.append(line)

        # Create a new CSV with BOM stripped from beginning of Employee ID cell
        with open(dest_path + file + '_corrected.csv', 'w', encoding='ASCII') as f:
            csv_writer = csv.writer(f, lineterminator = '\n')

            header = True
            for row in data:
                # Replace only the first header
                if header == True:
                    print(f'Eliminating Byte Order Marker from "{data[0][0]}"')
                    data[0][0] = 'Employee ID'
                    header = False

                # print(f"writing: {row}")
                csv_writer.writerow(row)

print("-" * 80)
print(f"{len(filelist)} successful file conversions saved to {dest_path}")
