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

#Выбор стороны
player_1 = ''
player_2 = ''
player_name = ''
def x_or_0():
    global player_1
    global player_2
    player_1 = input("Играете за + или за 0?\n")
    if player_1 == '+':
        player_2 = '0'
        print (f"{player_name} вы выбрали играть за Крестик (+)")
    elif player_1 == '0':
        player_2 = '+'
        print(f"{player_name} вы выбрали играть за Нолик (0)\n")
    else:
        print("Пожалуйста, ведите корректно + или 0!\n")
        x_or_0()

#Сделать ход
def move_player_1(step):
    if step == '00':
        if field[5] == '-':
            field[5] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '01':
        if field[6] == '-':
            field[6] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '02':
        if field[7] == '-':
            field[7] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '10':
        if field[9] == '-':
            field[9] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '11':
        if field[10] == '-':
            field[10] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '12':
        if field[11] == '-':
            field[11] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '20':
        if field[13] == '-':
            field[13] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '21':
        if field[14] == '-':
            field[14] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    elif step == '22':
        if field[15] == '-':
            field[15] = player_1
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_1 (step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    else:
        print ("Сделай верный ход!!!")
        move_player_1(step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    print_xo()
    get_result()
    print("Переход хода")
    move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))

def move_player_2(step):
    if step == '00':
        if field[5] == '-':
            field[5] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))
    if step == '01':
        if field[6] == '-':
            field[6] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))
    if step == '02':
        if field[7] == '-':
            field[7] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}) делайте ваш ход:"))
    if step == '10':
        if field[9] == '-':
            field[9] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))
    if step == '11':
        if field[10] == '-':
            field[10] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}) делайте ваш ход:"))
    if step == '12':
        if field[11] == '-':
            field[11] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))
    if step == '20':
        if field[13] == '-':
            field[13] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))
    if step == '21':
        if field[14] == '-':
            field[14] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))
    if step == '22':
        if field[15] == '-':
            field[15] = player_2
        else:
            print ("Данная клетка занята, выберите другую")
            move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))
    print_xo()
    get_result()
    print("Переход хода")
    move_player_1(step=input(f"{player_name} ({player_1}), делайте ваш ход:"))


#Выявляем победителя
def get_result():
    for i in win_str:
        if field[i[0]] == "+" and field[i[1]] == "+" and field[i[2]] == "+":
            print("Победил КРЕСТИК(+)!!!")
            quit()
        if field[i[0]] == "0" and field[i[1]] == "0" and field[i[2]] == "0":
            print("Победил НОЛИК(0)!!!")
            quit()
    drow()

def drow():
    while '-' not in  field[:]:
        print ("Победила ДРУЖБА!!!")
        quit()


# Игра
def game():
    print ("Добро пожаловать в игру КРЕСТИКИ-НОЛИКИ!!", end = "\n \n")
    global player_name
    player_name = (input("Как тебя зовут?").title())
    print ("Выберите сторону за кого будите играть?")
    x_or_0()
    print_xo()
    drow()
    move_player_1(step=input(f"{player_name} ({player_1}), делайте ваш ход:"))
    move_player_2(step=input(f"Игрок 2 ({player_2}), делайте ваш ход:"))




game()
