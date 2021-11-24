stack = []
def push(algo):
    stack.append(algo)
def pop():
    if len(stack)>0:
        return stack.pop()
    return None

push(1)
push(2)
push("piña")

print(pop())
print(pop())
print(pop())

print(pop())