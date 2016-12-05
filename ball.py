from coordinate import Coordinate
class Ball(object):

    def __init__(self, pos, name = ''):
        self._name = name
        self._pos  = pos
        self._velocity = Coordinate.origo()
        self._acc = Coordinate(0,-9.81*10) # gravity * scale


    def tick(self, s):
        """Perform one tick, s seconds have passed since last call."""
        if not self.is_alive:
            return False
        bp = 0.9 # bounce penalty
        upd = self._velocity + s * self._acc/2
        self._pos += s * upd;
        self._velocity += s * self._acc;
        if self._pos.y < 0:
            self._pos.y = -1 # dead object
            self._velocity = Coordinate.origo()
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

    @property
    def pos(self):
        return self._pos

    def __repr__(self):
        return 'Ball(name = %s, pos = %s)' % (self._name, self._pos)

    def is_alive(self):
        return self._pos.x >= 0
