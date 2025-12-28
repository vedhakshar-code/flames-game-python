name_1 = input("Enter a name: ")
name_2 = input("Enter another name: ")

name_1 = name_1.upper()
name_2 = name_2.upper()

if name_1 == name_2:
    print("Please enter two different names")

else:
    game = 'FLAMES'

    list_name_1 = []
    list_name_2 = []
    common_letters_FROM1 = []
    common_letters_FROM2 = []

    for i in name_1:
        list_name_1.append(i)

    for j in name_2:
        list_name_2.append(j)


    for k in list_name_1:
        if k in list_name_2:
            common_letters_FROM1.append(k)

    for l in list_name_2:
        if l in list_name_1:
            common_letters_FROM2.append(l)
    

    SUM = len(list_name_1) + len(list_name_2)
    COMMON_SUM = len(common_letters_FROM1) + len(common_letters_FROM2)
    RESULT_1 = SUM - COMMON_SUM

    game = ['F', 'L', 'A', 'M', 'E', 'S']

    index = 0
    while len(game) > 1:
        index = (index + RESULT_1 - 1) % len(game)
        game.pop(index)

    final = game[0]

    if final == 'F':
        print("FLAMES Result: Friends")
    elif final == 'L':
        print("FLAMES Result: Love")
    elif final == 'A':
        print("FLAMES Result: Affection")
    elif final == 'M':
        print("FLAMES Result: Marriage")
    elif final == 'E':
        print("FLAMES Result: Enemies")
    elif final == 'S':
        print("FLAMES Result: Siblings")