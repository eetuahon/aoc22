from collections import defaultdict
import re

def read_file():
    a = []
    f = open("input15", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    m = []
    for r in f:
        s = re.findall("[-]*\d+", r)
        sx, sy = (int(s[0]), int(s[1]))
        bx, by = (int(s[2]), int(s[3]))
        val = (sx, sy, bx, by)
        m.append(val)
    return m

def task1(f):
    t_s = set()
    line = set()
    row = 2000000 #task: count '#' on this row
    for r in f:
        sx, sy = (r[0], r[1])
        bx, by = (r[2], r[3])
        if sy == row:
            line.add(sx)
        if by == row:
            line.add(bx)
        d = abs(sx - bx) + abs(sy - by)
        dr = abs(sy - row)
        if d < dr: continue
        elif d == dr: t_s.add(sx)
        else:
            dx = d - dr
            xs = [i for i in range(sx-dx,sx+dx+1)]
            t_s |= set(xs)
    for i in line:
        if i in t_s:
            t_s.remove(i)
    print(len(t_s)) #15.1

def task2(f): #slow, takes 90s
    row = 4000000 #task: x,y = 0...4000000
    rs = defaultdict(lambda: list())
    yl, xl = (-1,-1)
    rl = set()
    sens = set()
    for r in f:
        sx, sy = (r[0], r[1])
        bx, by = (r[2], r[3])
        d = abs(sx - bx) + abs(sy - by)
        sens.add((sx,sy,d))
    for y in range(row+1):
        for s in sens:
            sx, sy, d = s
            dr = abs(sy-y)
            if d < dr: continue
            elif d == dr and sx >= 0 and sx <= row:
                rs[y].append((sx,sx))
            else:
                dx = d - dr
                left = max(0, sx-dx)
                right = min(row, sx+dx)
                rs[y].append((left, right))
        rs[y].sort()
        up = [j for i,j in rs[y]]
        if rs[y][0][0] != 0 or max(up) != row:
            yl = y
            break
        else:
            lim = -1
            for i in range(1, len(rs[y])):
                a1, a2 = rs[y][i-1]
                lim = max(a2, lim)
                b1, b2 = rs[y][i]
                if lim < b1 - 1:
                    yl = y
                    break
        if yl != -1: break
    for i in range(len(rs[yl])):
        x1, x2 = rs[yl][i]
        for x in range(x1,x2+1):
            rl.add(x)
    for i in range(row+1):
        if i not in rl:
            xl = i
            break
    t_s = xl * 4000000 + yl
    print(t_s) #15.2

def main():
    f = read_file()
    f = modify(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()