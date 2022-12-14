from collections import defaultdict
import copy

def read_file():
    a = []
    f = open("input14", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    m = defaultdict(lambda: " ")
    yl = 0
    for r in f:
        coords = r.split(" -> ")
        c = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in coords]
        for i in range(1,len(c)):
            x1, y1 = c[i-1]
            x2, y2 = c[i]
            if y1 > yl or y2 > yl: yl = max(y1,y2)
            if x1 == x2:
                y = min(y1, y2)
                yy = max(y1, y2)
                for j in range(y, yy+1):
                    m[(x1, j)] = "#"
            else:
                x = min(x1, x2)
                xx = max(x1, x2)
                for j in range(x, xx+1):
                    m[(j, y1)] = "#"
    return (m,yl)

def task1(f):
    t_s = -1
    m = f[0]
    yl = f[1]
    all_in = True
    while(all_in):
        t_s += 1
        x,y = (500,0)
        while(True):
            if y > yl:
                all_in = False
                break
            if m[(x,y+1)] == " ":
                y+=1
            elif m[(x-1,y+1)] == " ":
                x -= 1
                y += 1
            elif m[(x+1,y+1)] == " ":
                x += 1
                y += 1
            else:
                m[(x,y)] = "o"
                break
    print(t_s) #14.1

def task2(f):
    t_s = -1
    m = f[0]
    yl = f[1]
    while(True):
        t_s += 1
        x,y = (500,0)
        if m[(x,y)] == "o": break
        while(True):
            if y > yl:
                m[(x,y)] = "o"
                break
            if m[(x,y+1)] == " ":
                y+=1
            elif m[(x-1,y+1)] == " ":
                x -= 1
                y += 1
            elif m[(x+1,y+1)] == " ":
                x += 1
                y += 1
            else:
                m[(x,y)] = "o"
                break
    print(t_s) #14.2

def main():
    f = read_file()
    f = modify(f)
    task1(copy.deepcopy(f))
    task2(f)

if __name__== "__main__":
    main()