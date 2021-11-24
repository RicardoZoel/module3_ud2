import stackLIFO

class stackSumLIFO(stackLIFO.stackLIFO):


    def __init__(self):
        super().__init__()
        self.__sum=0

    def getSum(self):
        return self.__sum

    def push(self, elem):
        super().push(elem)
        self.__sum+=elem
    def pop(self):
        elem = super().pop()
        if elem !=None:
            self.__sum-=elem
        return elem
        
obsum = stackSumLIFO()
obsum.push(7)
obsum.push(5)
obsum.push(6)

print(obsum.pop)
print(obsum.pop)
print(obsum.pop)