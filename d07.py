def read_file():
    a = []
    f = open("input07", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def modify(f):
    path = ""
    dir = dict()
    dir.update({"/": dict()})
    for r in f:
        row = r.split(" ")
        if row[1] == "cd":
            if row[-1] == "..":
                path = "/".join(path.split("/")[:-2])
                path += "/"
            elif row[-1] == "/":
                path = "/"
            else:
                path += row[-1] + "/"
        elif row[1] == "ls":
            pass
        else:
            if row[0] == "dir":
                n_dir = path + row[1] + "/"
                if n_dir not in dir.keys():
                    dir.update({n_dir: dict()})
            else:
                dir[path].update({row[1]:int(row[0])})
    return dir

def insides(path, d, s):
    inside = []
    for dirs in d.keys():
        if dirs[:len(path)] == path and path != dirs: inside.append(dirs)
    size = s[path]
    for i in inside:
        size += s[i]
    return size

def task1(f):
    t_s = 0
    sizes, s2 = (dict(), dict())
    for dir in f.keys():
        sizes.update({dir: sum(f[dir].values())})
    for dir in f.keys():
        s2[dir] = insides(dir, f, sizes)
    for v in s2.keys():
        if s2[v] <= 100000:
            t_s += s2[v]
    print(t_s) #7.1

def task2(f):
    t_s = 999999
    sizes, s2 = (dict(), dict())
    for dir in f.keys():
        sizes.update({dir: sum(f[dir].values())})
    for dir in f.keys():
        s2[dir] = insides(dir, f, sizes)
    nd = 30000000 - 70000000 + s2["/"]
    for v in s2.values():
        if v < t_s and v > nd: t_s = v
    print(t_s) #7.2

def main():
    f = read_file()
    f = modify(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()