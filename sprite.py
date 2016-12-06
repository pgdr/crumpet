from coordinate import Coordinate
class Sprite(object):

    def __init__(self, pos, name = ''):
        self._name = name
        self._pos  = pos
        self._velocity = Coordinate.origo()
        self._acc = Coordinate(0,-9.81*50) # gravity * scale
        self._draw_right = ['rwalk1','rwalk2','rwalk3','rwalk4','rwalk5']
        self._draw_left  = ['lwalk1','lwalk2','lwalk3','lwalk4','lwalk5'].reverse()
        self._walkidx = 0


    def tick(self, s):
        """Perform one tick, s seconds have passed since last call."""
        bp = 0.9 # bounce penalty
        upd = self._velocity + s * self._acc/2
        self._pos += s * upd;
        self._velocity += s * self._acc;
        vx,vy = self._velocity.x, self._velocity.y
        if self._pos.y < 80:
            self._pos.y = 80
            vy = 0
        if self._pos.x < 5:
            self._pos.x = 5.0
            vx = 0
        if self._pos.x > 700:
            self._pos.x = 700.0
            vx = 0
        self._velocity = Coordinate(vx,vy)

    def jump(self):
        if self._pos.x < 100:
            self._velocity += Coordinate(500, 500)
        elif self._pos.x > 600:
            self._velocity += Coordinate(-500, 500)
        elif self._pos.y < 100:
            self._velocity += Coordinate(0, 250)
        self._pos.y += 10

    def right(self):
        self._velocity += Coordinate(10,0)

    def left(self):
        self._velocity += Coordinate(-10,0)

    def drawable(self):
        self._walkidx = 1 + ((self._pos.x) % 16)//4
        wdir = 'r'
        if self._velocity.x < 0:
            wdir = 'l'
        return 'graphics/%swalk%d.png' % (wdir,self._walkidx)

    @property
    def pos(self):
        return self._pos

    def __repr__(self):
        return 'Sprite(name = %s, pos = %s)' % (self._name, self._pos)
