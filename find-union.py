class Node():
    def __init__(self):
        self.val = 0
        self.rank = 0
        self.parent = self

def make_set(val):
    el = Node()
    el.val = val
    return el

def find(x):
    if x.parent == x: return x
    else:
        x.parent = find(x.parent)
        return x.parent

def union(x,y):
    a = find(x)
    b = find(y)

    if a == b: return

    if a.rank > b.rank:
        b.parent = a
        return

    if a.rank < b.rank:
        a.parent = b
        return
    #zostaje tylko opcja kiedy a.rank = b.rank
    b.parent = a
    a.rank += 1
    return

a = make_set(3)
b = make_set(2)
c = make_set(1)
d = make_set(9)

union(a,b)
union(b,c)
print(find(d).val)
