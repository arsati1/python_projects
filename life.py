import random
import time
size = 10
game_field = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(random.randint(0, 1))
    game_field.append(row)
for step in range(5):
    print("Такт", step)
    for i in range(size):
        line = ""
        for j in range(size):
            if game_field[i][j] == 1:
                line = line + "# "
            else:
                line = line + ". "
        print(line)
    print()
    new_field = []
    for i in range(size):
        new_field.append([0] * size)
    for i in range(size):
        for j in range(size):
            neighbors = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni = i + di
                    nj = j + dj
                    if ni >= 0 and ni < size and nj >= 0 and nj < size:
                        neighbors = neighbors + game_field[ni][nj]
            if game_field[i][j] == 0:
                if neighbors == 3:
                    new_field[i][j] = 1
            else:
                if neighbors < 2 or neighbors > 3:
                    new_field[i][j] = 0
                else:
                    new_field[i][j] = 1
    game_field = new_field
    time.sleep(0.5)