row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

def play_game():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    x = 0
    while x < 9:
        display(row1, row2, row3)
        enter_row = input("Enter the row you want to play (row1, row2, row3): ")
        if enter_row == "row1":
            position_index = int(input("Enter the index at which you want to play (0, 1, 2): "))
            value = input("Enter the value (X or O): ")
            row1[position_index] = value
        elif enter_row == "row2":
            position_index = int(input("Enter the index at which you want to play (0, 1, 2): "))
            value = input("Enter the value (X or O): ")
            row2[position_index] = value
        elif enter_row == "row3":
            position_index = int(input("Enter the index at which you want to play (0, 1, 2): "))
            value = input("Enter the value (X or O): ")
            row3[position_index] = value
        else:
            print("Please enter a valid row (row1, row2, row3).")
            continue

        x += 1

    display(row1, row2, row3)

play_game()