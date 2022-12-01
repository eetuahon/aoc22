def read_file():
    a = []
    f = open("input01", "r")
    b = []
    for i in f:
        if len(i) > 1:
            b.append(int(i.replace("\n","")))
        else:
            a.append(b)
            b = []
    a.append(b)
    f.close()
    return a

def task1(f):
    m_s = 0
    for i in f:
        s = sum(i)
        if s > m_s:
            m_s = s
    print(m_s) #1.1

def task2(f):
    s_l = [sum(i) for i in f]
    s_l.sort()
    m_s = sum(s_l[-3:])
    print(m_s) #1.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()