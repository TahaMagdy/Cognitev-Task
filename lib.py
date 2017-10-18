'''
    * Author: Taha Magdy
    * Date: 18th Oct, 2017


    * Task3
    =======
    * This is the `Module` that conatins myStack
    * Implementing the needed methods for test_stack.py
'''


class myStack:

    current_index = -1
    stack = []

    def add_item(self, *items):
        self.current_index += len(items)
        self.stack += items

    def pop_item(self):
        if self.current_index >= 0:
            pop = self.stack[self.current_index]
            del self.stack[self.current_index]
            self.current_index -= 1
            return pop
        elif self.current_index < 0:
            return []

    def count_items(self):
        return self.current_index + 1


mystack = myStack()
