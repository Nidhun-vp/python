# Get the number of rows and columns from the user
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# Initialize an empty matrix
matrix = []

# Populate the matrix with user input
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        element = int(input(f"Enter the element at row {i+1}, column {j+1}: "))
        row.append(element)
        print(row)
    matrix.append(row)
    # Using nested for loops to iterate through the matrix
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()  # Print a newline to separate rows