# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Point, Circle

circle = Circle(5, Point(0,0))

point1 = Point(3,4)
point2 = Point(6,0)
point3 = Point(5,0)

print(point1 in circle)
print(point2 in circle)
print(point3 in circle)

