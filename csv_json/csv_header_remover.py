# removes csv headers from all files in current working directory

import csv, os

# creates a directory called 'header removed' in the current working directory
os.makedirs('header_removed', exist_ok=True)

# looking through all the files in this directory and checking to see if they are csvs
for filename in os.listdir('.'):
    if not filename.endswith('.csv'):
        continue #skipping non-csv files

    print ('Removing header from ' + filename + '...')

    # creating a csv rows list so we can add all but the first row to a list
    csv_rows = []
    
    # opening the file and creating a reader object
    input_file_object = open(filename)
    reader_object = csv.reader(input_file_object)

    # looping through all rows and appending all except header
    for row in reader_object:
        if reader_object.line_num == 1: 
            continue                #skipping header row
        csv_rows.append(row) # we're saving this for later

    
    # closing the input file because we don't need it anymore
    input_file_object.close()

    # creating a new object in the subdirectory created above
    output_file_object = open(os.path.join('header_removed', filename), 'w', newline='')

    # creating a writer object from that file
    csv_writer = csv.writer(output_file_object)

    # using the csv_rows list created earlier to write rows to the new file
    for row in csv_rows:
        csv_writer.writerow(row)

    # saving and closing output file
    output_file_object.close()
    

    
