from pprint import pprint
boards = input('What size board do you want? (x by x) ')
win = input('How many connections are required to win? ')
print('Input your board \n')
matrix = []
rownum = 1
for i in range(int(boards)):
  myinput = input()
  splitted = myinput.split(' ')
  matrix.append(splitted)

pprint(matrix)

def getPossible(boardsize):
  posibilities = []
  for row in range(len(matrix)):
    yes = matrix[row]
    for column in range(len(yes)):
      current = matrix[row][column]
      i = 1
      #Check valid movements of indexes in matrix, exclude too high and negative indexes
      rowup = True
      rowdown = True
      columnup = True

      for additional in range(int(win)):
        if row + additional >= boardsize:
          rowup = False
        if row - additional <= -1:
          rowdown = False
        if column + additional >= boardsize:
          columnup = False

      #Find the values of these valid movements
      n1 = []
      n2 = []
      n3 = []
      n4 = []
      for additional in range(int(win)):
        if rowup:
          n1.append(matrix[row+additional][column])
        if columnup:
          n2.append(matrix[row][column + additional])
        if rowup and columnup:
          n3.append(matrix[row+additional][column + additional])
        if rowdown and columnup:
          n4.append(matrix[row-additional][column + additional])
      for i in [n1, n2, n3, n4]:
        if i != []:
          posibilities.append(i)
  return posibilities

def decidewinner():
  posibilities = getPossible(len(matrix))
  xwin = 0
  owin = 0
  for i in posibilities:
    same = len(set(i)) == 1
    if same and i[0] == 'x':
      xwin += 1
    if same and i[0] == 'o':
      owin += 1

  if xwin != 0 and owin == 0:
    print('X wins!')
  elif owin != 0 and xwin == 0:
    print('O wins!')
  elif owin == 0 and xwin == 0:
    print('No one wins')
  else:
    print('X and O wins??? Impossible!')
    
decidewinner()
