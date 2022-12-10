from collections import defaultdict

def read_file():
    a = []
    f = open("input10", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    g = defaultdict(lambda: ("busy", 0))
    i = 1
    for r in f:
        if "noop" in r:
            i += 1
            g[i] = ("noop", 0)
        else:
            i += 2
            m = r.split(" ")
            g[i] = (m[0], int(m[1]))
    return g

def task1(f):
    reg = 1
    t_s = []
    check = [20,60,100,140,180,220]
    for i in range(1,221):
        c = f[i]
        reg += c[1]
        if i in check:
            t_s.append(i * reg)
    print(sum(t_s)) #10.1

def task2(f):
    t_s = ""
    reg = 1
    d = defaultdict(lambda: -1)
    for i in range(1,241):
        c = f[i]
        reg += c[1]
        d[i] = reg
    for i in range(0,240):
        if i%40 == 0: t_s += "\n"
        if i % 40 == d[i+1] or i % 40 == d[i+1]+1 or i % 40 == d[i+1]-1:
            t_s += "#"
        else:
            t_s += "."
    print(t_s) #10.2

def main():
    f = read_file()
    f = modify(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()