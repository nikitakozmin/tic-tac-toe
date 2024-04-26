print('Добро пожаловать в игру "Крестики-нолики"!')
f = "1"
while f != "0":
    cells = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    field = '\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n'
    full_cells = []
    print(field)
    for cur_pl in (1, 2, 1, 2, 1, 2, 1, 2, 1):
        symb_cur_pl = ('x', 'o')[cur_pl-1]
        
        # Выбор клетки игроком
        while True:
            num_cell = int(input(
                f"Игрок №{cur_pl}({symb_cur_pl}) выберите клетку: "))
            if num_cell in full_cells:
                print('Клетка уже занята, повторите попытку.')
            else:
                full_cells.append(num_cell)
                break
        cells[(num_cell-1)//3][(num_cell-1)%3] = symb_cur_pl
        field = field.replace(str(num_cell), symb_cur_pl); print(field)
        
        # Проверка выигрыша по горизонатали
        if len(set(cells[(num_cell-1)//3])) == 1:
            print(f"Выиграл игрок №{cur_pl}({symb_cur_pl})")
            break
        
        # Проверка выигрыша по вертикали
        if len(set(list(zip(*cells))[(num_cell-1)%3])) == 1:
            print(f"Выиграл игрок №{cur_pl}({symb_cur_pl})")
            break
        
        # Проверка выигрыша по диагоналям
        if num_cell in {1, 4, 9}:
            if len({cells[0][0], cells[1][1], cells[2][2]}) == 1:
                print(f"Выиграл игрок №{cur_pl}({symb_cur_pl})")
                break
        if num_cell in {3, 4, 7}:
            if len({cells[2][0], cells[1][1], cells[0][2]}) == 1:
                print(f"Выиграл игрок №{cur_pl}({symb_cur_pl})")
                break
        
    else:
        print('Победила дружба!')
    f = input('Хотите повторить игру? Введите "0", чтобы закончить: ')
