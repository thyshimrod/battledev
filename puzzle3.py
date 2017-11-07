# *******
# * Read input from STDIN
# * Use echo or print to output your result, use the /n constant at the end of each result line.
# * Use:
# *      local_print (variable );
# * to display simple variables in a dedicated area.
# * ***/
import sys

size = 0
lines = []
i = 0
for line in sys.stdin:
    if i == 0:
        size = int(line.rstrip('\n'))
    else:
        lines.append(line.rstrip('\n'))

    i += 1

map = [[0 for x in range(size)] for y in range(size)]

for l in range(size):
    for i in range(size):
        map[i][l] = lines[i][l]

tab = []
def lookAround(x,y,map,size,tab):
    for j in (-1,0, 1):
        for i in (-1,0,1):
            if (y + j) >= 0 and ( y + j) < size:
                if (x+i)>=0 and (x+i) < size:
                    if map[y+j][x+i] == ".":
                        if (str(y+j) + "/" + str(x+i)) not in tab:
                            tab.append(str(y+j) + "/" + str(x+i))



for y in range(size):
    for x in range(size):
        if map[y][x] == "X":
            lookAround(x,y,map,size,tab)

print(len(tab))

