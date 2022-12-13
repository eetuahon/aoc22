import functools

def read_file():
    a = []
    f = open("input13", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def listify(l):
    if len(l) == 0: return []
    if "[" not in l:
        return [int(i) for i in l.split(",")]
    a = []
    while "[" in l:
        s = l.find("[")
        lvl = 0
        for i in range(s, len(l)):
            if l[i] == "[": lvl +=1
            if l[i] == "]":
                lvl -= 1
                if lvl == 0:
                    a.append(listify(l[s+1:i]))
                    l = l[:s] + "-1" + l[i+1:]
                    break
    nl = [int(i) for i in l.split(",")]
    while -1 in nl:
        ns = a.pop(0)
        nl[nl.index(-1)] = ns
    return nl

def modify(f):
    p = []
    for i in range(0,len(f),3):
        first = listify(f[i][1:-1])
        second = listify(f[i+1][1:-1])
        p.append((first,second))
    return p

def compare(a,b):
    al, bl = (len(a), len(b))
    if len(b) > len(a):
        l = len(b)
    else:
        l = len(a)
    for i in range(l):
        if i >= al: return 1
        if i >= bl: return 0
        av = a[i]
        bv = b[i]
        if type(av) == int and type(bv) == int:
            if av > bv: return 0
            if bv > av: return 1
        elif type(av) == list and type(bv) == list:
            o = compare(av,bv)
            if o >= 0: return o
        elif type(av) == list and type(bv) == int:
            o = compare(av, [bv])
            if o >= 0: return o
        else:
            o = compare([av], bv)
            if o >= 0: return o
    return -1

def comp(a,b):
    if compare(a,b) == 1: return -1
    else: return 1

def task1(f):
    t_s = 0
    for i in range(len(f)):
        t_s += compare(f[i][0], f[i][1]) * (i+1)
    print(t_s) #13.1

def task2(f):
    t_s = 1
    all = []
    a1 = [[2]]
    a2 = [[6]]
    all.append(a1)
    all.append(a2)
    for i in f:
        all.append(i[0])
        all.append(i[1])
    all_s = sorted(all, key=functools.cmp_to_key(comp))
    for i in range(len(all_s)):
        if all_s[i] == a1 or all_s[i] == a2: t_s *= (i+1)
    print(t_s) #13.2

def main():
    f = read_file()
    f = modify(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()