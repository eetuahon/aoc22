from collections import defaultdict
import math

def read_file():
    a = []
    f = open("input08", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    g = []
    for r in f:
        g.append([int(x) for x in list(r)])
    return g

def task1(f):
    t_s = set()
    y_l = len(f)
    x_l = len(f[0])
    for y in range(y_l):
        l = -1
        for x in range(x_l):
            if f[y][x] > l:
                t_s.add((x, y))
                l = f[y][x]
    for x in range(x_l):
        l = -1
        for y in range(y_l):
            if f[y][x] > l:
                t_s.add((x, y))
                l = f[y][x]
    for y in range(y_l):
        l = -1
        for x in range(x_l-1, -1, -1):
            if f[y][x] > l:
                t_s.add((x, y))
                l = f[y][x]
    for x in range(x_l):
        l = -1
        for y in range(y_l-1, -1, -1):
            if f[y][x] > l:
                t_s.add((x, y))
                l = f[y][x]
    print(len(t_s)) #8.1

def task2(f):
    t_s = 0
    view = defaultdict(lambda: [])
    y_l = len(f)
    x_l = len(f[0])
    coord = []
    for y in range(1,y_l-1):
        for x in range(1,x_l-1):
            coord.append((x,y))
    for c in coord:
        v = 1
        x, y = (c[0],c[1])
        cv = f[y][x]
        for xc in range(x+1, x_l-1): ##+1
            if f[y][xc] < cv:
                v += 1
            else:
                break
        view[c].append(v)
        v = 1
        for xc in range(x-1, 0, -1): ##+1
            if f[y][xc] < cv:
                v += 1
            else:
                break
        view[c].append(v)
        v = 1
        for yc in range(y+1, y_l-1): ##+1
            if f[yc][x] < cv:
                v += 1
            else:
                break
        view[c].append(v)
        v = 1
        for yc in range(y-1, 0, -1): ##+1
            if f[yc][x] < cv:
                v += 1
            else:
                break
        view[c].append(v)
    for x in view.values():
        z = math.prod(x)
        if z > t_s: t_s = z
    print(t_s) #8.2

def main():
    f = read_file()
    f = modify(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()