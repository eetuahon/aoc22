def read_file():
    a = []
    f = open("input03", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    t_s = 0
    a = []
    for i in f:
        i1 = i[:int(len(i)/2)]
        i2 = i[int(len(i)/2):]
        for c in i1:
            if c in i2:
                a.append(c)
                break
    for i in a:
        iv = ord(i)
        if i.islower():
            t_s += iv - 96
        else:
            t_s += iv - 38
    print(t_s) #3.1

def task2(f):
    t_s = 0
    a = []
    for i in range(0, len(f), 3):
        a.append((f[i], f[i+1], f[i+2]))
    for i in a:
        for c in i[0]:
            if c in i[1] and c in i[2]:
                iv = ord(c)
                if c.islower():
                    t_s += iv - 96
                else:
                    t_s += iv -38
                break
    print(t_s) #3.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()