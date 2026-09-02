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
    table = utils.restructure_lines_into_table(lines)
    print(table)

    # remove first row as a header (separate data table from header)
    header = table.pop(0)
    print(header)
    # print(table)

    for x in table:
        print(x)

    # convert numeric columns
    utils.convert_column_to_numeric(table,1)
    utils.convert_column_to_numeric(table,2)

    print(table)
    # TODO: write a pretty_print() function to print out 
    # the table in a nice grid like function

if __name__== "__main__":
    main()