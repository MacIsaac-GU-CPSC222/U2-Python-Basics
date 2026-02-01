import utils


def main():
# load file into table
    filename = "data.csv"
    lines = utils.load_lines_from_file(filename)
    print(lines)
# TASK: clean the newlines 
    utils.clean_lines(lines)
    print(lines)
# restructure into 2D list of rows with column values
# remove first row as a header (separate data table from header)

# convert numeric columns

# TODO: write a pretty_print() function to print out the table in a 
# nice grid like function

if __name__== "__main__":
    main()