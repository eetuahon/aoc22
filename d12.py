import copy, sys

m = []
mm = []
mem = []
sd = -1

def read_file():
    a = []
    f = open("input12", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    maze = []
    xl = len(f[0])
    yl = len(f)
    for y in range(yl):
        r = []
        for x in range(xl):
            letter = f[y][x]
            if letter == "S":
                r.append(ord("a")-96)
                s = (x,y)
            elif letter == "E":
                r.append(ord("z")-96)
                e = (x,y)
            else:
                r.append(ord(letter)-96)
        maze.append(r)
    return (maze, s, e)

def move(c, t, l):
    global m, mm, mem
    x, y = c
    tx, ty = t
    if c == t:
        mem = []
        return
    v = m[y][x]
    yl = len(m)
    xl = len(m[0])
    add = 0
    if x < xl-1:
        if mm[y][x+1] == -1 and m[y][x+1] <= v+1:
            mm[y][x+1] = l+1
            mem.append((l+1,(x+1,y)))
            add += 1
    if y < yl-1:
        if mm[y+1][x] == -1 and m[y+1][x] <= v+1:
            mm[y+1][x] = l+1
            mem.append((l+1,(x,y+1)))
            add += 1
    if x > 0 and not ((y == 0 or y == yl-1) and tx > x):
        if mm[y][x-1] == -1 and m[y][x-1] <= v+1:
            mm[y][x-1] = l+1
            mem.append((l+1,(x-1,y)))
            add += 1
    if y > 0:
        if mm[y-1][x] == -1 and m[y-1][x] <= v+1:
            mm[y-1][x] = l+1
            mem.append((l+1,(x,y-1)))
            add += 1
    if add == 0: return
    mem.sort()
    while len(mem) > 0:
        n = mem.pop(0)
        move(n[1],t,n[0])
    return

def move_down(c, tl, l):
    global m, mm, mem, sd
    x, y = c
    v = m[y][x]
    if v == tl:
        mem = []
        sd = l
        return
    yl = len(m)
    xl = len(m[0])
    add = 0
    if x < xl-1:
        if mm[y][x+1] == -1 and m[y][x+1] >= v-1:
            mm[y][x+1] = l+1
            mem.append((l+1,(x+1,y)))
            add += 1
    if y < yl-1:
        if mm[y+1][x] == -1 and m[y+1][x] >= v-1:
            mm[y+1][x] = l+1
            mem.append((l+1,(x,y+1)))
            add += 1
    if x > 0:
        if mm[y][x-1] == -1 and m[y][x-1] >= v-1:
            if mm[y][x-1] == -1 and m[y][x-1] >= v-1:
                mm[y][x-1] = l+1
                mem.append((l+1,(x-1,y)))
                add += 1
    if y > 0:
        if mm[y-1][x] == -1 and m[y-1][x] >= v-1:
            mm[y-1][x] = l+1
            mem.append((l+1,(x,y-1)))
            add += 1
    if add == 0: return
    mem.sort()
    while len(mem) > 0:
        n = mem.pop(0)
        move_down(n[1],tl,n[0])
    return

def task1(f):
    global m, mm, sd
    m = f[0]
    sx, sy = f[1]
    ex, ey = f[2]
    row = [-1 for i in range(len(m[0]))]
    mm = [copy.copy(row) for i in range(len(m))]
    mm[sy][sx] = 0
    move((sx, sy), (ex, ey), 0)
    t_s = mm[ey][ex]
    print(t_s) #12.1

def task2(f):
    global m, mm, mem, sd
    m = f[0]
    sx, sy = f[2]
    ex, ey = f[1]
    tl = m[ey][ex]
    row = [-1 for i in range(len(m[0]))]
    mm = [copy.copy(row) for i in range(len(m))]
    mm[sy][sx] = 0
    move_down((sx, sy), tl, 0)
    t_s = sd
    print(t_s) #12.2

def main():
    sys.setrecursionlimit(7000)
    f = read_file()
    f = modify(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()