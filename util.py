import csv

def read_file(file, tc):
    with open(file) as file:
        reader = csv.reader(file, delimiter='|')
        line_count=0
        header=[]
        dict={}
        for row in reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                cell_count=0
                if (tc == row[0]):
                    for cell in row:
                        dict.setdefault(header[cell_count], cell)
                        cell_count +=1
                line_count += 1

        # Return test data as a Dictionary
        return dict