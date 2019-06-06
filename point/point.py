import _point

class Point():
    def __init__(self, x=None, y=None):
        if x:
            self.p = _point.lib.get_point(x, y)
        else:
            self.p = _point.lib.get_default_point()
        
    def __repr__(self):
        return '({0}, {1})'.format(self.p.x, self.p.y)

    def show_point(self):
        _point.lib.show_point(self.p)

    def move_point(self):
        _point.lib.move_point(self.p)

    def move_point_by_ref(self):
        ppoint = _point.ffi.new("Point*", self.p)
        _point.lib.move_point_by_ref(ppoint)
        self.p = ppoint
