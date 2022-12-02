def read_file():
    a = []
    f = open("input02", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    t_s = 0
    a = []
    for i in f:
        i = i.replace("A","1").replace("B","2").replace("C","3")
        i = i.replace("X","1").replace("Y","2").replace("Z","3")
        s = i.split(" ")
        a.append((int(s[0]), int(s[1])))
        t_s += int(s[1])
    for i in a:
        if i[0] == i[1]:
            t_s += 3
        if i[1] - i[0] == 1 or i[1] - i[0] == -2:
            t_s += 6
    print(t_s) #2.1

def task2(f):
    t_s = 0
    a = []
    for i in f:
        i = i.replace("A","1").replace("B","2").replace("C","3")
        i = i.replace("X","0").replace("Y","3").replace("Z","6")
        s = i.split(" ")
        a.append((int(s[0]), int(s[1])))
        t_s += int(s[1])
    for i in a:
        if i[1] == 6:
            t_s += i[0] % 3 + 1
        if i[1] == 3:
            t_s += i[0]
        if i[1] == 0:
            t_s += ((i[0]-2) % 3) + 1
    print(t_s) #2.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()