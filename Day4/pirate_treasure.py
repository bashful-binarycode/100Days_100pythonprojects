def treasure(position:int):
    row1 = ['😀', '😀', '😀']
    row2 = ['😀', '😀', '😀']
    row3 = ['😀', '😀', '😀']

    matrix = [row1, row2, row3]
    true_position = list(str(position))
    coloumn = int(true_position[0]) - 1
    row = int(true_position[1]) - 1
    
    print(f"Before\n{row1}\n{row2}\n{row3}")
    
    if row == 0:
        row1[coloumn] = 'X'
    elif row == 1:
        row2[coloumn] = 'X'
    else:
        row3[coloumn] = 'X'
    
    print(f"After\n{row1}\n{row2}\n{row3}")
treasure(32)