from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


class FPoint():
    """
    FPoint represents a point on the floating-point Cartesian plane
    (i.e., it is an (x, y) pair, with x and y represented as floats).
    """
    x = float()  # The horizontal coordinate
    y = float()  # The vertical coordinate

    def __init__(self, x=0.0, y=0.0):
        self.set_xy(x, y)

    # TODO check code on set/add/scale usage (with fp, or constant factor k)

    def set_fp(self, fp):
        self.x = fp.x
        self.y = fp.y

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def add_k(self, k):
        return FPoint(self.x + k, self.y + k)

    def add_fp(self, fp):
        return FPoint(self.x + fp.x, self.y + fp.y)

    def scale_k(self, k):
        return FPoint(self.x * k, self.y * k)

    def scale_fp(self, fp):
        return FPoint(self.x * fp.x, self.y * fp.y)

    def __str__(self):
        return f"( {self.x:.2f}, {self.y:.2f})"
