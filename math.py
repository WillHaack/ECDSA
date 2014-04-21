class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __unicode__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

def pointAddition(p, q):
    lam = (q.y - p.y) / (q.x - p.x)
    xR = lam ** 2 - p.x - q.x
    yR = lam * (p.x - xR) - p.y
    return Point(xR, yR)

def pointDouble(p):
    lam = ((3 * (p.x ** 2)) + 1) / (2 * p.y)
    xR = lam ** 2 - 2 * p.x
    yR = lam * (p.x - xR) - p.y
    return Point(xR, yR)

def doubleAndAdd(d, p):
    q = Point(0,0)
    for i in list(bin(d)[2:])[::-1]:
        if (i == '1'):
            q = pointAddition(p, q)
        p = pointDouble(p)
    return q




P = Point(1, (3 ** .5))
Q = Point(2, (11 ** .5))
print(pointAddition(P,Q).__unicode__())
print(pointDouble(P).__unicode__())
