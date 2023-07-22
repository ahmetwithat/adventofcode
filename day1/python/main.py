f = open("input.txt", "r")
file_from_data = f.read()
file_from_data = file_from_data.split("\n")
end=0
start=0
arrindex=[]
data=[]
for i in range(len(file_from_data)):
  if file_from_data[i] == '':
    end = i
  if end != 0:
    for j in range(end-start):
      arrindex.append(file_from_data[start+j])
    data.append(arrindex)
    start = end+1
    end = 0
    arrindex = []

f.close()
calories=0
elvelist=[]
for elf in data:
  for item in elf:
    calories += int(item)
  elvelist.append(calories)
  calories = 0
total = 0
for i in range(3):
  biggestnumber=0
  for elf in range(len(elvelist)):
    if elvelist[elf] > biggestnumber:
      biggestnumber = elvelist[elf]
  total+=biggestnumber
  print(biggestnumber)
  elvelist.pop(elvelist.index(biggestnumber))
  

print(total)