class Point:
    def __init__(self,xval,yval):
        self.x = xval
        self.y = yval

    def __eq__(self,other):  # ==
        return (self.y==other.y and self.x==other.x)

    def __lt__(self,other):  # <
        if self.y<other.y:
            return True
        elif self.y>other.y:
            return False
        elif self.x < other.x:
            return True
        else:
            return False
  def __repr__(self):
        return f"x-val:{self.x},y-val:{self.y}"
