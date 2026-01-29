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
    pass

def clean_lines(lines):
    """
    removes ending whitespace from a list of lines
    """
    pass

def restructure_lines_into_table(lines):
    """
    takes a list where each row is a line and converts it into a 2D list
    splits each line by a comma
    """
    pass

def convert_column_to_numeric(table, column_index):
    """
    converts every item in a column of a table to a float
    """



def pretty_print(header, table):
    """
    prints out the header and table such that it appears like a nice grid
    """


# load file into table



# TASK: clean the newlines 



# restructure into 2D list of rows with column values
# remove first row as a header (separate data table from header)



# convert numeric columns


# TODO: write a pretty_print() function to print out the table in a 
# nice grid like function
