import re, copy

def read_file():
    a = []
    f = open("input06", "r")
    for i in f:
        a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    t_s = 1
    s = f[0]
    mem = [s[i] for i in range(3)]
    for i in range(3, len(s)):
        n = s[i]
        mem.append(n)
        if len(set(mem)) == 4:
            t_s += i
            break
        mem.pop(0)
    print(t_s) #6.1

def task2(f):
    t_s = 1
    s = f[0]
    mem = [s[i] for i in range(13)]
    for i in range(13, len(s)):
        n = s[i]
        mem.append(n)
        if len(set(mem)) == 14:
            t_s += i
            break
        mem.pop(0)
    print(t_s) #6.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()