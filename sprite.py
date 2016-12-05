from coordinate import Coordinate
class Sprite(object):

    def __init__(self, pos, name = ''):
        self._name = name
        self._pos  = pos
        self._velocity = Coordinate.origo()
        self._acc = Coordinate(0,-98.1) # gravity
        self._drawable = ['E','N']


    def tick(self, s):
        """Perform one tick, s seconds have passed since last call."""
        bp = 0.9 # bounce penalty
        upd = self._velocity + s * self._acc/2
        self._pos += s * upd;
        self._velocity += s * self._acc;
        if self._pos.y < 50:
            self._pos.y = 50
            self._velocity = self._velocity.flip_vertical(bp)
        if self._pos.x < 5:
            self._pos.x = 5.0
            self._velocity = self._velocity.flip_horizontal(bp)
        if self._pos.x > 700:
            self._pos.x = 700.0
            self._velocity = self._velocity.flip_horizontal(bp)

    def jump(self):
        self._velocity += Coordinate(0, 20)

    def right(self):
        self._velocity += Coordinate(10,0)

    def left(self):
        self._velocity += Coordinate(-10,0)

    def drawable(self):
        if self._velocity.x > 0:
            self._drawable[0] = 'E'
        if self._velocity.x < 0:
            self._drawable[0] = 'W'
        if self._velocity.y > 0:
            self._drawable[1] = 'N'
        if self._velocity.y < 0:
            self._drawable[1] = 'S'
        return 'graphics/' + ''.join(self._drawable) + '.png'

    @property
    def pos(self):
        return self._pos

    def __repr__(self):
        return 'Sprite(name = %s, pos = %s)' % (self._name, self._pos)
