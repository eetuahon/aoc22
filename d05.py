import re, copy

def read_file():
    a = []
    f = open("input05", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    l = len(f[0])
    a = []
    b = []
    d = dict()
    for r in f:
        if "[" in r:
            s = [r[i] for i in range(1, l, 4)]
            a.append(s)
        elif "move" in r:
            x = [int(n) for n in re.findall("\d+", r)]
            b.append((x[0], x[1], x[2]))
    ll = len(a[0])
    for i in range(1, ll+1):
        d.update({i:[]})
    for r in a:
        for i in range(ll):
            if r[i] != " ":
                d[i+1].insert(0, r[i])
    return (d, b)

def task1(f):
    t_s = ""
    d = f[0]
    moves = f[1]
    for m in moves:
        for i in range(m[0]):
            l = d[m[1]].pop()
            d[m[2]].append(l)
    for i in range(len(d)):
        t_s += d[i+1][-1]
    print(t_s) #5.1

def task2(f):
    t_s = ""
    d = f[0]
    moves = f[1]
    for m in moves:
        reminder = []
        for i in range(m[0]):
            reminder.insert(0, d[m[1]].pop())
        d[m[2]].extend(reminder)
    for i in range(len(d)):
        t_s += d[i+1][-1]
    print(t_s) #5.2

def main():
    f = read_file()
    f = modify(f)
    task1(copy.deepcopy(f))
    task2(f)

if __name__== "__main__":
    main()