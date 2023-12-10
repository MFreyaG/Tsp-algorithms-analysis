class Stack:
    def __init__(self):
        self.stack = []
        
    def add_item(self, item):
        self.stack.append(item)
    
    def remove_item(self):
        if len(self.stack) != 0:
            item = self.stack.pop()
            return item

        return None