#!/usr/bin/python3
''' Module Square '''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return("[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        ''' Get Size '''
        return self.width

    @size.setter
    def size(self, value):
        '''Set Size '''
        self.width = value
        self.height = value

    def update(self, *args, **keywords):
        ''' Update square with args '''
        idx = 0
        if args:
            while idx < len(args):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.size = args[idx]
                if idx == 2:
                    self.x = args[idx]
                if idx == 3:
                    self.y = args[idx]
                idx += 1
        else:
            for arg in keywords:
                setattr(self, arg, keywords.get(arg))

    def to_dictionary(self):
        ''' Definitioin of dictionary '''
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
