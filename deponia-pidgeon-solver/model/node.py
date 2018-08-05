
class Node(object):

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}: ({}, {})".format(self.name, self.x, self.y)
