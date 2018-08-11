import sys


class Node(object):

    def __init__(self, x, y, is_center=False, is_active=False):
        self.x = x
        self.y = y
        self.is_center = is_center
        self.is_active = is_active

    def __repr__(self):
        return "(({}, {}) - (c: {}, a: {}))".format(self.x, self.y, self.is_center, self.is_active)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return (self.x == other.x
                and self.y == other.y
                and self.is_center == other.is_center
                and self.is_active == other.is_active)


# null object pattern...or something like that
class InvalidNode(Node):
    def __init__(self):
        super(InvalidNode, self).__init__(sys.maxint, sys.maxint)
