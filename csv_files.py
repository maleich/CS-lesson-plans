import csv


filename = 'text_files/Marine_CSV_sample.csv'

with open(filename) as data:
    reader = csv.reader(data)   # reads csv and stores data in reader
    header_row = next(reader)   # returns next line in file as list
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Extracting data

    wind_direction = []
    for row in reader:
        w_dir = int(row[31])
        wind_direction.append(w_dir)
    print(wind_direction)

