print(  '''Вас приветсвует игра
      Крестики Нолики
_________________________________________________
Правила игры просты:
Небоходимо выставить в линию или по диагонали Х или 0
____________________________________________________
Как ходить : у каждой клетки есть номер в линию и номер в высоту.
Сначала необходимо ввести команду которая идет по линии, а затем выбрать по высоте.
Ввод команды вносится через пробел ''')
def poleone():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(pole):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if pole[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(pole[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


pole = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    poleone()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "0"

    if win():
        break

    if count == 9:
        print(" Ничья!")
        break