
# Klasse der kører in-place i stedet. 
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def x(self):
        return self._x
    
    def y(self):
        return self._y
    
    def moved(self, dx, dy):
        return Point(self._x + dx, self._y + dy)
    
    def move(self, dx, dy):
        self._x += dx
        self._y += dy

