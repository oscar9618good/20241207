rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to be printed: " )

for i in range(rows):
    for j in range(cols):
        print(symbol, end=" ")       
    print()                     # print() is used to move to the next line