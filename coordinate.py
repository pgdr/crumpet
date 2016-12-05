from math import sqrt

class Coordinate(object):
    def __init__(self, x=0, y=0, copy=None):
        if copy is None:
            self._x = x
            self._y = y
        else:
            self._x = copy.x
            self._y = copy.y

    def flip_vertical(self, penalty=1):
        return Coordinate(self.x, -self.y*penalty)
    def flip_horizontal(self, penalty=1):
        return Coordinate(-self.x*penalty, self.y)

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        self._x = val
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        self._y = val

    @classmethod
    def origo(cls):
        return Coordinate(0,0)
    def __repr__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)

    def __len__(self):
        return 2
    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, idx):
        if idx == 0:
            return self.x
        if idx == 1 or idx == -1:
            return self.y
        raise IndexError('A coordinate has 2 elements.  Invalid idx %d.' % idx)

    def __setitem__(self, idx, val):
        if idx == 0:
            self.x = val
            return self
        if idx == 1 or idx == -1:
            self.y = val
            return self
        else:
            raise IndexError('Cannot set index %d.' % idx)

    def __add__(self, otr):
        if isinstance(otr, Coordinate):
            return Coordinate(self.x + otr.x, self.y + otr.y)
        if isinstance(otr, float) or isinstance(otr, int):
            return Coordinate(self.x + otr, self.y + otr)
        raise ArgumentError('Cannot add Coordinate with %s!' % type(otr))

    def __mul__(self, scalar):
        return Coordinate(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Coordinate(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Coordinate(self.x / scalar, self.y / scalar)

    def __sub__(self, otr):
        return Coordinate(self.x - otr.x, self.y - otr.y)

    def __eq__(self, otr):
        return self.x == otr[0] and self.y == otr[1]
    
    def __abs__(self):
        return Coordinate(abs(self.x), abs(self.y))

    def distance(self, otr):
        x1, x2 = self.x, otr.x
        y1, y2 = self.y, otr.y
        dx = (x1-x2)**2
        dy = (y1-y2)**2
        return sqrt(dx+dy)
