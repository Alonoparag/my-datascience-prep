def border(cell_count):
    #We use this function to dynamically print borders
    base_cell = "+"+"-"*4+"+"
    additional_cell = "-"*4+"+"
    total_cells = base_cell+additional_cell*cell_count
    print(total_cells)
    
def cell_row(cell_count):
    base_cell = "/"+" "*4+"/"
    additional_cell = " "*4+"/"
    total_cells = base_cell+additional_cell*cell_count
    i = 0
    while(i < 4):
        print(total_cells)
        i+=1

def grid(rows, columns):
    border(columns)
    i_rows = 0
    while i_rows < rows:
        cell_row(columns)
        border(columns)
        i_rows += 1

rows = input("Please enter the number of desired rows")
columns = input("Please enter the number of desired rows")

grid(rows,columns)