import time


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.insert(0, data)

    def is_empty(self):
        return self.stack == []

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def reverse_string(self):
        while True:
            if len(self.stack) == 0:
                break
            else:
                print(self.stack.pop(0), end="\n")


if __name__ == "__main__":
    s1 = Stack()
    s1.push("Cat")
    s1.push("Dog")

    print(s1.size())
    print(s1.peek())
    print(s1.size())
    print(s1.pop())

    s1.push("C")
    s1.push("a")
    s1.push("t")

    print(s1.reverse_string())