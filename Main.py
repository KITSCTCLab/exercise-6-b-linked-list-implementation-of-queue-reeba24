class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    n = Node(data)
    n.next = self.head
    self.head = n

  def pop(self) -> None:
    # Write your code here
    if self.head is not None:
      self.head = self.head.next

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    itr = self.head
    while itr is not None:
      print(itr.data, end = "=>")
      itr = itr.next
    print("None")


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
