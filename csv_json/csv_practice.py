# reading and writing csvs

import csv, os

input_file = open('example.csv')
input_reader = csv.reader(input_file)

for row in input_reader:
    print('Row #' + str(input_reader.line_num) + ' ' + str(row))

# opens file in write mode; newline is needed for correct formatting
output_file = open('output.csv', 'w', newline='')

# creates a writer object
output_writer=csv.writer(output_file)

# putting our data in the right 
output_writer.writerow(['spam', 'bacon', 'eggs', 'cheese'])
output_file.close() #does not save unless you close the file

# next up, delimiters and lineterminators - tabs and double spaced
# make sure to use the .tsv files extension
output_file_2 = open('output2.tsv', 'w', newline='')
output_writer_2 = csv.writer(output_file_2, delimiter='\t', lineterminator='\n\n')

# writing all the rows
output_writer_2.writerow(['spam', 'grapes', 'eggs', 'cheese'])
output_writer_2.writerow(['spam', 'grapes', 'bacon', 'cheese'])
output_writer_2.writerow(['sausage', 'grapes', 'eggs', 'cheese'])

# saving and closing
output_file_2.close()

# next up, DictReader and DictWriter
# these work well with files that have hedder rows, and they use dictionaries

print('DictReader and Writer time')
input_file_3 = open('exampleWithHeader.csv')
dict_reader = csv.DictReader(input_file_3)

for row in dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

# if your document does not have a header row, you can supply keys for it

input_file_4 = open('example.csv')
dict_reader_4 = csv.DictReader(input_file_4, ['Time', 'Name', 'Amount'])

for row in dict_reader_4:
    print(row['Time'], row['Name'], row['Amount']) #these have to match the arguments above

# writing a header row to a file (and adding rows)

output_file_5 = open('output5.csv', 'w', newline='')
output_writer_5 = csv.DictWriter(output_file_5, ['Name', 'Pet', 'Phone'])
output_writer_5.writeheader()
output_writer_5.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_writer_5.writerow({'Name': 'Gia', 'Pet': 'mouse', 'Phone': '525-1234'})

output_file_5.close()
