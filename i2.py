import loaded1
from prettytable import PrettyTable
from turtle import Turtle,Screen

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('green')
# timmy.forward(100)
# my_screen  = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


table = PrettyTable()

data = [
    {
        "name": "Alice",
        "age": 30
    },
    {
        "name": "Bob",
        "city": "New York"
    }
]

# Get all unique keys from the dictionaries (assuming consistent keys across sub-arrays)
all_keys = set(key for d in data for key in d.keys())

# Set table headers (using all unique keys)
table.field_names = list(all_keys)

# Loop through each sub-array (dictionary)
for outer_dict in data:
    # Create a temporary row to store values for each key
    row = []
    for key in all_keys:
        # Access value using get() for potential missing keys
        value = outer_dict.get(key)
        row.append(value)  # Add value to the row

    # Add the row to the table
    table.add_row(row)

# Print the table
print(table)

