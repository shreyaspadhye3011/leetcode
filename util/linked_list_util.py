# Note: when you add new functions to this class, they might not be recognized by files outside as those will be referencing old binary (.pyc) file

# Temp solution: 
# 1. delete .pyc file 
# 2. create a new file and copy all code. Run it & then run the file where you're referencing it

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data=None):
        curr = self.head 
        while curr.next != None:
            curr = curr.next
        
        new_node = node(data)
        curr.next = new_node
    
    def display(self):
        curr = self.head
        elems = []
        while curr.next != None:
            curr = curr.next
            elems.append(curr.data)
        print(elems)

    def temp(self):
        print("HEllop!")
