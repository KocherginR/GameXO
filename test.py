side = ''

def x_or_0():
    global side
    side = input("Выберите сторону!\nИграете за + или за 0?\n")
    if side == '+':
        print ("Вы выбрали играть за Крестик (+)")
    elif side == '0':
        print("Вы выбрали играть за Нолик (0)\n")
    else:
        print("Пожалуйста, ведите корректно + или 0!\n")
        x_or_0()

move_player_1 (step=input("Игрок 1, делайте ваш ход:"))
x_or_0()

print(side)


