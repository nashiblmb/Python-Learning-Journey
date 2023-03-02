#Practice exercise creating treasure map, works with input of up to a value of 3 in double digits e.g. 33, first 3 is for column second is for row

#Initialisation of rows
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")


position = input("Where do you want to put the treasure?: ")

#iterating through rows to place the "x"
for i in range(len(map)):
    if i+1 == int(position[1]):
        map[i][int(position[0])-1] = "x"
    print(map[i])
    
