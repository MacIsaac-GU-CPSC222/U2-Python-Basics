# FILES
# a file stores data on a file system
# "on disk"

# goal: is to load the contents of data.csv
# into our python program memory
# stored as a 2D list

# 3-step file processing template
# 1. open file
# 2. process file (e.g., read or write)
# 3. close the file

def load_lines_from_file(filename):
    """
    opens the file <filename>, reads the file into a list, closes the file
    returns the list
    """
    r_file = open(filename, "r")
    lines = r_file.readlines()
    r_file.close()
    return lines


def clean_lines(lines):
    """
    removes ending whitespace from a list of lines
    """
    for ind in range(len(lines)):
        lines[ind] = lines[ind].strip()

def restructure_lines_into_table(lines):
    """
    takes a list where each row is a line and converts it into a 2D list
    splits each line by a comma
    """
    table = []
    for line in lines:
        table.append(line.split(','))
    return table

def convert_column_to_numeric(table, column_index):
    """
    converts every item in a column of a table to a float
    """
    for i in range(len(table)):
        table[i][column_index] = float(table[i][column_index])

def pretty_print(header, table):
    """
    prints out the header and table such that it appears like a nice grid
    """
    pass