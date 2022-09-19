class Stack:

    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def isEmpty(self):
        return not self.stack

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def is_balance(string):
    brackets_dict = {'[': ']', '(': ')','{': '}',}
    stack = Stack()
    for s in string:
        if s in brackets_dict:
            stack.push(s)
        elif s == brackets_dict.get(stack.peek()):
            stack.pop()
        else:
            return 'Несбалансированно'
    if stack.isEmpty():
        flag = 'Сбалансированно'
    else:
        flag = 'Несбалансированно'
    return flag


if __name__ == '__main__':
    stack_ = Stack()
    stack_.push(1)
    stack_.push(2)
    stack_.push(3)
    stack_.push(4)
    print(stack_.size())
    print(stack_.isEmpty())
    print(stack_.peek())
    stack_.pop()
    stack_.pop()
    print(stack_.size())
    stack_.pop()
    stack_.pop()
    stack_.pop()
    print(stack_.isEmpty())
    print(stack_.peek())

    check_list = ['[([])((([[[]]])))]{()}', '}{}', '{{[(])]}}']

    for list_ in check_list:
        print(is_balance(list_))


