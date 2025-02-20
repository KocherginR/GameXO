#Создание поля
field = [" ", 0, 1, 2,
            0, "-", "-", "-",
            1, "-", "-", "-",
            2, "-", "-", "-"]

#Возможные варианты победы
win_str = [[5, 6, 7],
          [9, 10, 11],
          [13, 14, 15],
          [5, 9, 13],
          [6, 10, 14],
          [7, 11, 15],
          [5, 10, 15],
          [7, 10, 13]]



#Вывод поля для игры в крестики-нолики на экран
def print_xo():
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2], end=" ")
    print(field[3])

    print(field[4], end=" ")
    print(field[5], end=" ")
    print(field[6], end=" ")
    print(field[7])

    print(field[8], end=" ")
    print(field[9], end=" ")
    print(field[10], end=" ")
    print(field[11])

    print(field[12], end=" ")
    print(field[13], end=" ")
    print(field[14], end=" ")
    print(field[15])
    print("------------------------Чтобы сделать ход,\nнеобходимо использовать систему координат,\n"
          "как в морском бою!------------------------\n")

#Сделать ход
def move(step,symbol):
    if step == '00':
        field[5] = symbol
    if step == '01':
        field[6] = symbol
    if step == '02':
        field[7] = symbol
    if step == '10':
        field[9] = symbol
    if step == '11':
        field[10] = symbol
    if step == '12':
        field[11] = symbol
    if step == '20':
        field[13] = symbol
    if step == '21':
        field[14] = symbol
    if step == '22':
        field[15] = symbol
    print_xo()
    get_result()

#Выявляем победителя
def get_result():
    for i in win_str:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "Победил игрок X!!!"
            print(win, end = '\n')
        if field[i[0]] == "0" and field[i[1]] == "0" and field[i[2]] == "0":
            win = "Победил игрок 0!!!"
            print(win, end = '\n')
        else:
            move(step=input("Ваш ход:"), symbol=input("X или 0:").title())


# Игра
def game():
    print_xo()
    move(step = input("Ваш ход:"), symbol = input("X или O:").title())




game()
