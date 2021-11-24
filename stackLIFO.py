class stackLIFO():
    def __init__(self):
        self.__stack=[]

    def push(self,elem):
        self.__stack.append(elem)
    def pop(self):
        if len(self.__stack)>0:
            return self.__stack.pop()
        return None
    def __private(self):
        pass

stack = stackLIFO()
stack.push(5)
stack.push(6)
stack.push(2)

print(stack._stackLIFO__stack)
print(stack.__dict__)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.pop())