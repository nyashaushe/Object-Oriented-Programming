

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self):
        import math
        
        return math.sqrt(self.x ** 2 + self.y**2)

    def __gt__(self, other):  # greater than
        return self.length() > other.length()

    def __ge__(self, other):  # greater than or equal to
        return self.length() >= other.length()
        
    def __lt__(self, other):  # less than
        return self.length() < other.length()

    def __le__(self, other):  # less than or equal to
        return self.length() <= other.length()
    
    def __add__(self,p):
        return self.x  + p.x , self.y + p.y
    
    def __sub__(self,p):
        return self.x  - p.x , self.y - p.y



# We are going to compare points based on their lengths
    

p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p1+p2
p6 = p3-p4

#isLess = p1 <= p2  # This is False
#print(isLess)
print(p6)


