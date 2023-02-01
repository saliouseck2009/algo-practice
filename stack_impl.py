class stack:
  def __init__(self):
    self.__index = []

  def __len__(self):
    return len(self.__index)

  def push(self,item):
    self.__index.insert(0,item)

  def peek(self):
    if len(self) == 0:
      raise Exception("peek() called on empty stack.")
    return self.__index[0]

  def pop(self):
    if len(self) == 0:
      raise Exception("pop() called on empty stack.")
    return self.__index.pop(0)

  def __str__(self):
    return str(self.__index)


s = stack()
s.push("a")
s.push("b")
print(s.peek())
s.push("c")
print(s.pop())
print(str(s))