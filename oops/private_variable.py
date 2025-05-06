class P:
    def __init__(self, xval):
        self.x = xval
   
    @property
    def x(self):   # used to get the value of instance attribute '__x'
        return self.__x

    @x.setter
    def x(self,val):
        if val>100:
            self.__x = 100
        elif x<=0:
            self.__x = 0
        else:
            self.__x = val
