class Node:
  def __init__(self, key):
    self.key = key

class Heap:
  def __init__(self, max_size):
    self.the_list = [None] * max_size
    self.max_size = max_size
    self.current_size = 0

  def is_empty(self):
    return self.current_size == 0

  def insert(self, key):
    if self.current_size == self.max_size:
      return False
    new_node = Node(key)
    self.the_list[self.current_size] = new_node
    self.current_size += 1
    self.percolate_up(self.current_size - 1)
    return True

  def percolate_up(self, index):
    parent = int((index - 1) / 2 )
    bottom = self.the_list[index]

    while index > 0 and self.the_list[parent].key < bottom.key:
      self.the_list[index] = self.the_list[parent]
      index = parent
      parent = int((parent - 1)/ 2)

    self.the_list[index] = bottom

  def pop(self):
    root = self.the_list[0]
    self.current_size -=1
    self.the_list[0] = self.the_list[self.current_size]
    self.percolate_down(0)
    return root

  def percolate_down(self, index):
    larger_child = 0
    top = self.the_list[index]

    while index < self.current_size / 2:
      left_child = 2 * index + 1
      right_child = left_child + 1

      if right_child < self.current_size and \
        self.the_list[left_child].key < self.the_list[right_child].key:
        larger_child = right_child
      else:
        larger_child =left_child
      if top.key >= self.the_list[larger_child].key:
        break

      self.the_list[index] = self.the_list[larger_child]
      index = larger_child
    
    self.the_list[index] = top


if __name__ == "__main__":
  heap = Heap(31)
  heap.insert(72)
  heap.insert(44)
  heap.insert(53)
  heap.insert(21)
  heap.insert(66)
  heap.insert(100)
  heap.insert(84)
  heap.insert(35)
  heap.insert(19)
  heap.insert(90)

  heap.pop()

  for i in heap.the_list:
    if i is None:
      print("N", end=", ")
    else:
      print(i.key, end=", ")

  print()
