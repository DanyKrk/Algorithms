class Employee:
    def __init__(self,name,fun):
        self.name = name
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1

def f(v): # wartość najlepszej imprezy w Tv
    if v.f != -1: return v.f
    x = v.fun
    for u in v.emp:
        x+= g(u)
    y = g(v)
    v.f = max(x,y)
    if(v.f == x): print(v.name)
    return v.f

def g(v): #wartość najlepszej imprezy w Tv, kiedy v nie idzie:
    if v.g != -1: return v.g
    x = 0
    for u in v.emp:
        x+=f(u)
    v.g = x
    return v.g


def make_best_party(chef):
    return f(chef)


a = Employee("a",7)
b = Employee("b",3)
c = Employee("c",5)
d = Employee("d",100)
e = Employee("e",13)
h = Employee("h",17)
i = Employee("i",19)
j = Employee("j",23)
k = Employee("k",29)

a.emp = [b, c, d]
b.emp = [e, h]
c.emp = [i]
d.emp = [j, k]

print(make_best_party(a))