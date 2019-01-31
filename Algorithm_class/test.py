<<<<<<< HEAD
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def get_area(self):
        return 3.14*self.r**2

    def get_perimeter(self):
        return 3.14*2*self.r

    def get_center(self):
        return (self.center.x, self.center.y)

    def print(self):
        print(f"Circle: {self.get_center()}, r: {self.r}" )




p1 = Point(0,0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()


p2 = Point(4,5)
c2 = Circle(p2,1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()


def F(c, a=1, b=3):
    print(a,b,c)

F(1,2,3)
F(1,2)
F(1)


=======
for n in range(1,11):
    print(2**n-1 )
>>>>>>> 29697f04b1e3d92fe9ab82e1b94b49b87cf2d61f
