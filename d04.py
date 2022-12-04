def read_file():
    a = []
    f = open("input04", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    t_s = 0
    a = [(x.split(",")[0], x.split(",")[1]) for x in f]
    a = [(int(p[0].split("-")[0]), int(p[0].split("-")[1]), int(p[1].split("-")[0]), int(p[1].split("-")[1])) for p in a]
    for p in a:
        if p[0] >= p[2] and p[1] <= p[3]: t_s += 1
        if p[2] >= p[0] and p[3] <= p[1]: t_s += 1
        if p[0] == p[2] and p[1] == p[3]: t_s -= 1
    print(t_s) #4.1

def task2(f):
    t_s = 0
    a = [(int(p[0].split("-")[0]), int(p[0].split("-")[1]), int(p[1].split("-")[0]), int(p[1].split("-")[1])) for p in [(x.split(",")[0], x.split(",")[1]) for x in f]]
    for p in a:
        if p[2] <= p[1] and p[2] >= p[0]: t_s += 1
        if p[0] <= p[3] and p[0] >= p[2] and not (p[2] <= p[1] and p[2] >= p[0]): t_s += 1
    print(t_s) #4.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()