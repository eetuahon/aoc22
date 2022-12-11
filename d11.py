from collections import defaultdict
import copy

def read_file():
    a = []
    f = open("input11", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    monk = []
    mem = []
    id = 0
    for r in f:
        if len(r) == 0:
            monk.append(mem)
            mem = []
        elif "Monkey" in r:
            mem.append(id)
            id += 1
        elif "Starting" in r:
            ls = r.split(": ")[1]
            sn = [int(i) for i in ls.split(", ")]
            mem.append(sn)
        elif "Operation" in r:
            o = r.split(" ")
            if o[-1] == "old":
                op, on = ("**", 2)
            else:
                op, on = (o[-2], int(o[-1]))
            mem.append((op,on))
        else:
            i = r.split(" ")[-1]
            mem.append(int(i))
    monk.append(mem)
    return monk

def task1(f):
    mb = defaultdict(lambda: 0)
    for i in range(20):
        for m in f:
            for s in m[1]:
                if m[2][0] == "**":
                    s2 = s * s
                elif m[2][0] == "*":
                    s2 = s * m[2][1]
                else:
                    s2 = s + m[2][1]
                s2 = s2 // 3
                if s2 % m[3] == 0:
                    f[m[4]][1].append(s2)
                else:
                    f[m[5]][1].append(s2)
                mb[m[0]] += 1
            m[1] = []
    t_s = [i for i in mb.values()]
    t_s.sort()
    print(t_s[-1] * t_s[-2]) #11.1

def task2(f):
    mb = defaultdict(lambda: 0)
    multi = 1
    for i in f:
        multi *= i[3]
    for i in range(10000):
        for m in f:
            for s in m[1]:
                if m[2][0] == "**":
                    s2 = s * s
                elif m[2][0] == "*":
                    s2 = s * m[2][1]
                else:
                    s2 = s + m[2][1]
                s2 %= multi
                if s2 % m[3] == 0:
                    f[m[4]][1].append(s2)
                else:
                    f[m[5]][1].append(s2)
                mb[m[0]] += 1
            m[1] = []
    t_s = [i for i in mb.values()]
    t_s.sort()
    print(t_s[-1] * t_s[-2]) #11.2

def main():
    f = read_file()
    f = modify(f)
    task1(copy.deepcopy(f))
    task2(f)

if __name__== "__main__":
    main()