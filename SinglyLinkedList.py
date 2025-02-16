class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next =  self.head
            self.head = new_node

    def insertIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return
            
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_mode = Node(data)
            new_mode.next = current_node.next
            current_node.next = new_mode
        else:
            print("Index not existing.")

    def removefirstnode(self):
        if (self.head == None):
            return
        self.head = self.head.next    

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position!= index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not existing.")

    def removelastNode(self):
        if (self.head == None):
            return
        
        current_node = self.head
        while (current_node.next != None and current_node.next.next != None):
            current_node = current_node.next
        
        current_node.next = None

    def removeatIndex(self, index):
        if self.head is None:
            return
        
        current_node = self.head
        position = 0

        if index == 0:
            self.removefirstNode()
        else:
            while current_node != None and position < index - 1:
                position += 1
                current_node = current_node.next
            
            if current_node is None or current_node.next is None:
                print("Index not existing.")
            else:
                current_node.next = current_node.next.next


    def removeNode(self, data):
        current_node = self.head

        if current_node.data == data:
            self.removefirstnode()
            return
        
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next


    def printList(self):
        current_node = self.head
        if not current_node:
            print("Empty List.")
            return

        while(current_node):
            print (current_node.data)
            current_node = current_node.next

    def sizeList(self):
        size = 0
        if (self.head):
            current_node = self.head
        if not current_node:
            print("List is empty.")
            
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0


Llist = LinkedList()

while True: 
    answer = input(
        "What would you like to do? \n"
        "\n 1 to insert first node \n" 
        "\n 2 insert index \n" 
        "\n 3 remove first node \n" 
        "\n 4 insert end node \n" 
        "\n 5 update node \n" 
        "\n 6 remove last node \n" 
        "\n 7 remove at index \n" 
        "\n 8 remove nod \n"
        "\n 9 print list \n"
        "\n 0 exit \n"
        )

    if answer == "1":
        val = int(input("What number would you like to insert?\n"))
        Llist.insertBegin(val)

    elif answer == "2":
        index, val = map(int, input("Input index and number (seperated by space): \n").split(' '))
        Llist.insertIndex(val, index)

    elif answer == "3":
        Llist.removefirstnode()

    elif answer == "4":
        val = int(input("Enter number to insert at the end:\n "))
        Llist.insertEnd(val)   

    elif answer == "5":
        index, val = map(int, input("Enter index and new value (seperated by space):\n ").split(' '))
        Llist.updateNode(val, index)

    elif answer == "6":
        Llist.removelastNode()

    elif answer == "7":
        index = int(input("Enter index of node to remove:\n "))
        Llist.removeatIndex(index)

    elif answer == "8":
        val = int(input("Enter node to remove:\n "))
        Llist.removeNode(val)

    elif answer == "9":
        print("Current List:\n ")
        Llist.printList()

    elif answer == "0":
        print("Exiting.\n")
        break

    else:
        print("Invalid choice.\n")