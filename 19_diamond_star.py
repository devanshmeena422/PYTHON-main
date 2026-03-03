rows = int(input())

# Upper part
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))

# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)