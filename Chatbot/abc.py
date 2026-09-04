matrix_of_dicts = [
    [   # Outer index 0
        {"name": "Alice", "role": "Admin"},  # Inner index 0
        {"name": "Bob", "role": "User"}      # Inner index 1
    ],
    [   # Outer index 1
        {"name": "Charlie", "role": "Guest"} # Inner index 0
    ]
]

for index,list in enumerate(matrix_of_dicts):
    print(f"index: {index} and list_items: {list}")
#print(len(matrix_of_dicts))
# x = ('apple', 'banana', 'cherry')
# y=enumerate(x)
# print(list(y))