

class BinarySearch():
  
  def __init__(self, step = 1, theLength = 10):
    self.alist = [i for i in range(0 + step, theLength * step, step)]
    print self.alist
    self.length = theLength
    self.first = 0
    self.last = self.length
    self.mid = (self.first + self.last) // 2
    self.found = False
    self.counter = 0 
    self.dictvals = self.search(9)
  def search(self,val):
    while self.first<=self.last and not self.found:
        self.mid=(self.first+self.last)//2
        self.counter+=1
        if self.alist[self.mid]==val:
            self.found = True
        else:
            if val<=self.alist[self.mid]:
                self.last=self.mid
                self.search(val)
            else:
                self.first=self.mid
                self.search(val)
                
        
        return {'count':self.counter,'index':self.mid}
x=BinarySearch(20,2)
print(x.dictvals)