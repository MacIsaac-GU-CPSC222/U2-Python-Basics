# Files
# a file stores data on a disk/file system
# many times in plaintext

# 3 step process
# 1. open file
# 2. process the file (read or write)
# 3. close file

def load_lines_from_file(filename):
    """
    open the file <filename>, read the file into a list, and close the file

    return the list
    """
    r_file = open(filename, "r")
    lines = r_file.readlines()
    
    r_file.close()
    return lines

def clean_lines(lines):
    """
    remove the ending whitespace from a list of lines

    returns nothing (it will modify the original list)

    .strip()
    """
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def restructure_lines_into_table(lines):
    """
    takes a list where each row is a line and converts it into a 2D list splitting each line by a comma

    returns new 2D list

    [["Date", "Calories Burned", "Steps,], 
     ["3/8/21"...],
     ["3/9/21"...]
    ]
    """
    table = []
    for line in lines:
        table.append(line.split(","))
    return table

def convert_column_to_numeric(data, column_ind):
    """
    convert every item in a column of a table to a float
    """
    for row_ind in range(len(data)):
        data[row_ind][column_ind] = float(data[row_ind][column_ind])
