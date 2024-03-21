class Rect:
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains_point(self, x2, y2):
        return x2>=self.x and self.x<=(self.x+self.w) and y2>=self.y and y2<=(self.y+self.h)
