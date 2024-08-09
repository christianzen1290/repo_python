class User:

    def __init__(self, x):
        self.x = x


user_1 = User(3)
print(user_1.x)
user_1.id = "1"
user_1.username = "test"

user_2 = User(4)
user_2.id = "2"
user_2.name = "war"



# Define a multidimensional array using dictionaries
matrix = {
    'row1': {'col1': 1, 'col2': 2, 'col3': 3},
    'row2': {'col1': 4, 'col2': 5, 'col3': 6},
    'row3': {'col1': 7, 'col2': 8, 'col3': 9}
}

# Use nested for loops to iterate over the dictionary of dictionaries
for row_key, row_value in matrix.items():
    print(f"{row_key}: ", end="")
    for col_key, col_value in row_value.items():
        print(f"{col_key}={col_value} ", end="")
    print()  # Print a new line after each row
