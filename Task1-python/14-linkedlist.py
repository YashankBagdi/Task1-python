class Node:
    def __init__(self, data):
        self.data, self.next = data, None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, x):
        if not self.head: self.head = Node(x)
        else:
            last = self.head
            while last.next: last = last.next
            last.next = Node(x)
    def delete_end(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next: temp = temp.next
        temp.next = None
    def display(self):
        nodes, curr = [], self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(nodes) or "List is empty.")
my_list = LinkedList()
k=int(input("how many elements: "))
print("enter elements: ")
for i in range(k):
    j=int(input())
    my_list.insert_end(j)
print("After inserting elements:")
my_list.display()
my_list.delete_end()
print("After deleting from the end:")
my_list.display()
my_list.delete_end()
print("After deleting from the end again:")
my_list.display()


