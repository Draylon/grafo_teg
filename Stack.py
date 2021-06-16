class MStack:
  def __init__(self):
    self.list = []

  def push(self,item):
    self.list.append(item)

  def pop(self):
    return self.list.pop()

  def not_empty(self):
    return len(self.list) != 0
