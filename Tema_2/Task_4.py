# Print the header row
header = "    "

for column in range(1, 11):
    header += f"{column:4}"

print(header)

# Print the multiplication table
for row in range(1, 11):
    line = f"{row:>3} "

    for column in range(1, 11):
        result = row * column
        line += f"{result:4}"

    print(line)