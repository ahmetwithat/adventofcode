# X = LOSE
# Y = DRAW
# Z = WIN



with open("input.txt", 'r') as my_file:
  f = my_file.read()

data=f.split('\n')

for i in range(len(data)):
  arr = data[i].split(' ')
  data[i] = arr

for i in data:
  match i[0]:
    case 'A':
      i[0] = 1
    case 'B':
      i[0] = 2
    case 'C':
      i[0] = 3

def DeterminePlay(elvesmove, outcome):
  match outcome:
    case 'X':
      play = (elvesmove+2)%3
      if play == 0:
        play = 3
    case 'Y':
      play = elvesmove
    case 'Z':
      play = (elvesmove+1)%3
      if play == 0:
        play = 3
  return play

def CalculateScore(elvesmove, yourmove):
  outcomescore = 0
  match abs(elvesmove-yourmove):
    case 0:
      outcomescore = 3
    case 1:
      if elvesmove > yourmove:
        outcomescore = 0
      else:
        outcomescore = 6
    case 2:
      if elvesmove < yourmove:
        outcomescore = 0
      else:
        outcomescore = 6
  return outcomescore+yourmove

totalscore = 0
for i in data:
  totalscore+= CalculateScore(i[0], DeterminePlay(i[0], i[1]))

print(totalscore)
