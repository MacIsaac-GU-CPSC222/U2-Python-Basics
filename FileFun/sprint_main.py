import sprint_utils
def main():
    lines = sprint_utils.load_lines_from_file("data.csv")
    print("lines:", lines)
    # TASK: clean the newlines 
    sprint_utils.clean_lines(lines)
    print("lines:", lines)
    # restructure into 2D list of rows with column values
    table = sprint_utils.restructure_lines_into_table(lines)
    header = table.pop(0)
    print(header)
    print(table)
    sprint_utils.convert_column_to_numeric(table, 1) # 1 corresponds to Calories Burned
    sprint_utils.convert_column_to_numeric(table, 2) # 2 corresponds to Steps
    print("after conversion")
    print(header)
    print(table)
    # TODO: write a pretty_print() function to print out the table in a 
    # nice grid like function
    # GS adding after class
    sprint_utils.pretty_print(header, table)

if __name__=="__main__":
    main()