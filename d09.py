def read_file():
    a = []
    f = open("input09", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    g = []
    for r in f:
        m = r.split(" ")
        g.append((m[0], int(m[1])))
    return g

def move(h, t, d):
    hx, hy = (h[0], h[1])
    tx, ty = (t[0], t[1])
    if d == "R":
        hx += 1
    elif d == "U":
        hy += 1
    elif d == "L":
        hx -= 1
    else:
        hy -= 1
    if hx - tx == 2 or hx - tx == -2:
        ty += hy - ty
        if hx > tx: tx += 1
        else: tx -= 1
    elif hy - ty == 2 or hy - ty == -2:
        tx += hx - tx
        if hy > ty: ty += 1
        else: ty -= 1
    return (hx, hy, tx, ty)

def move_many(l, d):
    hx, hy = l[0]
    tx, ty = l[1]
    hx, hy, tx, ty = move((hx,hy),(tx,ty),d)
    l[0] = (hx, hy)
    l[1] = (tx, ty)
    for i in range(2,10):
        hx, hy = l[i-1]
        tx, ty = l[i]
        if hx - tx == 2 or hx - tx == -2:
            if hy > ty: ty += 1
            elif hy < ty: ty -= 1
            if hx > tx: tx += 1
            else: tx -= 1
        elif hy - ty == 2 or hy - ty == -2:
            if hx > tx: tx += 1
            elif hx < tx: tx -= 1
            if hy > ty: ty += 1
            else: ty -= 1
        l[i] = (tx, ty)
    return

def task1(f):
    t_s = set()
    hx, hy = (0,0)
    tx, ty = (0,0)
    for m in f:
        for i in range(m[1]):
            hx, hy, tx, ty = move((hx,hy),(tx,ty),m[0])
            t_s.add((tx,ty))
    print(len(t_s)) #9.1

def task2(f):
    t_s = set()
    coord = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    for m in f:
        for i in range(m[1]):
            move_many(coord, m[0])
            t_s.add(coord[9])
    print(len(t_s)) #9.2

def main():
    f = read_file()
    f = modify(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()