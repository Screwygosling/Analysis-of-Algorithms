class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.last = None  

    def insertemptyList(self, value):
        if self.last is not None:
            return self.last

        new_node = Node(value)
        self.last = new_node
        new_node.next = new_node  
        return self.last

    def insertBegin(self, value):
        if self.last is None:
            return self.insertemptyList(value)

        new_node = Node(value)
        new_node.next = self.last.next
        self.last.next = new_node
        return self.last

    def insertEnd(self, value):
        if self.last is None:
            return self.insertemptyList(value)

        new_node = Node(value)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node  
        return self.last

    def insertatpos(self, data, position):
        if self.last is None:
            if position != 1:
                print("Invalid position")
                return self.last
            return self.insertemptyList(data)

        new_node = Node(data)
        curr = self.last.next

        if position == 1:
            new_node.next = curr
            self.last.next = new_node
            return self.last

        for i in range(position - 2):
            curr = curr.next
            if curr == self.last.next:
                print("Invalid position")
                return self.last

        new_node.next = curr.next
        curr.next = new_node

        if curr == self.last:
            self.last = new_node

        return self.last

    def delfirstNode(self):
        if self.last is None:
            print("List is empty")
            return None

        head = self.last.next

        if head == self.last:  
            self.last = None
        else:
            self.last.next = head.next

        return self.last

    def delLast(self):
        if self.last is None:
            print("List is empty")
            return None

        head = self.last.next

        if head == self.last:  
            self.last = None
            return self.last

        curr = head
        while curr.next != self.last:
            curr = curr.next

        curr.next = head
        self.last = curr

        return self.last

    def delspecificNode(self, key):
        if self.last is None:
            print("List is empty.")
            return None

        curr = self.last.next
        prev = self.last

        if curr == self.last and curr.data == key:  
            self.last = None
            return self.last

        if curr.data == key: 
            self.last.next = curr.next
            return self.last

        while curr != self.last and curr.data != key:
            prev = curr
            curr = curr.next

        if curr.data == key:
            prev.next = curr.next
            if curr == self.last:
                self.last = prev
        else:
            print(f"Node with data {key} not found.")

        return self.last

    def printList(self):
        if self.last is None:
            print("The list is empty.")
            return

        head = self.last.next
        while True:
            print(head.data, end=" -> ")
            head = head.next
            if head == self.last.next:
                break
        print()


Llist = LinkedList()

while True:
    answer = input(
        "What would you like to do? \n"
        "1: Insert first node\n"
        "2: Insert at position\n"
        "3: Remove first node\n"
        "4: Insert at end\n"
        "5: Delete last node\n"
        "6: Remove node by value\n"
        "7: Print list\n"
        "0: Exit\n"
    )

    if answer == "1":
        val = int(input("Enter the value to insert: "))
        Llist.insertBegin(val)

    elif answer == "2":
        pos, val = map(int, input("Enter position and value: ").split())
        Llist.insertatpos(val, pos)

    elif answer == "3":
        Llist.delfirstNode()

    elif answer == "4":
        val = int(input("Enter the value to insert at the end: "))
        Llist.insertEnd(val)

    elif answer == "5":
        Llist.delLast()

    elif answer == "6":
        val = int(input("Enter the value to remove: "))
        Llist.delspecificNode(val)

    elif answer == "7":
        Llist.printList()

    elif answer == "0":
        print("Exiting.")
        break

    else:
        print("Invalid choice.")
