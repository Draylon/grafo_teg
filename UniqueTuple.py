class UniqueTuple:
    def __init__(self,left,right):
        self.u = left
        self.v = right
    def hasElement(self,e):
        if self.u==e or self.v == e:
            return True
        else:
            return False
    
    def getList(self):
        return [self.u,self.v]


    def getSet(self):
        return set(self.getList())

    def __eq__(self, value):
        if value.getSet() == self.getSet():
            return True
        else: return False