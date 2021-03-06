field = list(range(1,10))

def tic_tac_toe_field(field):
    # рисует поле для игры в крестики - нолики
   print("-" * 15)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
      print("-" * 15)

def take_input(player_token):
    # запрашивает от игрока цифру в поле,
    # на место которой поставить X или 0
    # сравнивает, что введенная информация точно число
    # и это число от 1 до 9
   valid = False
   while not valid:
      player_answer = input("Where do we put the " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Invalid input. Are you sure you entered a number?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(field[player_answer-1]) not in "X0"):
            field[player_answer-1] = player_token
            valid = True
         else:
            print("This cell is already taken!")
      else:
        print("Invalid input. Enter a number from 1 to 9.")

def check_win(board):
    # сравнивает индексы комбинаций на игровом поле
    # с кортежем выиграшных коминаций индексов
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False

def main(field):
    # заменяет цифры на поле (в окне) на Х или 0
    # согласно введённой информации (цифры) от игроков.
    # сравнивает индексы в заменённых полях (окнах)
    #  с кортежем индексов выигрышных комбинаций
    counter = 0
    win = False
    while not win:
        tic_tac_toe_field(field)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("0")
        counter += 1
        if counter > 4:
           tmp = check_win(field)
           if tmp:
              print(tmp, "won!")
              win = True
              break
        if counter == 9:
            print("The game ended in a draw!")
            break
    tic_tac_toe_field(field)
main(field)

input("Press Enter to exit!")

