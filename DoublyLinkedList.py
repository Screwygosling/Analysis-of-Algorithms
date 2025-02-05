class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    
    def insertafterNode(self, target_data, data):

        if self.head is None:
            print("List is empty.")
            return
                
        current = self.head
        while current and current.data != target_data:
            current = current.next

        if current is None:
            print("Target node not found.")
            return
        
        new_node = Node(data)
        new_node.prev = current
        new_node.next = current.next

        if current.next:
            current.next.prev = new_node
        
        current.next = new_node

    def insertbeforeNode(self, target_data, data):

        if self.head is None:
            print("List is empty.")
            return
                
        current = self.head
        while current and current.data != target_data:
            current = current.next

        if current is None:
            print("Target node not found.")
            return
        
        new_node = Node(data)
        new_node.next = current
        new_node.prev = current.prev

        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node 
        
        current.prev = new_node

    def insertatEnd(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current
        return self.head
        
    def deleteatBegin(self):

        if self.head is None:
            print("List is empty")
            return 
        
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        
    
    def deleteatpos(self, position):
        if self.head is None:
            print("List is empty")
            return None
        
        if position < 0:
            print("Invalid positon")
            return self.head
        
        if position == 0:
            if self.head.next:
                self.head.next.prev = None
            return self.head.next
        
        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return self.head
        
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

        del current
        return self.head

    def deleteatend(self):
        if self.head is None:
            print("List is empty")
            return None
        
        if self.head.next is None:
            self.head = None
            return None
        
        current = self.head
        while current.next:
            current = current.next

        current.prev.next = None
        del current
        


    def display(self):
        current = self.head
        while current:
            print(current.data, end = " <-> ")
            current = current.next
        print("None")


Llist = LinkedList()

while True: 
    try: 
        answer = input(
            "What would you like to do? \n"
            "\n 1 to insert at beginning \n" 
            "\n 2 insert after node \n" 
            "\n 3 insert before node \n" 
            "\n 4 insert at end \n" 
            "\n 5 delete at beginning \n" 
            "\n 6 delete at position \n" 
            "\n 7 delete at end \n"
            "\n 8 Display list \n"
            "\n 0 Exit \n"
            )

        if answer == "1":
            val = int(input("Enter the value to insert at the beginning\n"))
            Llist.insertBegin(val)

        elif answer == "2":
                target = int(input("Enter the target node value: "))
                val = int(input("Enter the value to insert after the target node: "))
                Llist.insertafterNode(target, val)

        elif answer == "3":
            target = int(input("Enter the target node value: "))
            val = int(input("Enter the value to insert before the target node: "))
            Llist.insertbeforeNode(target, val)


        elif answer == "4":
            val = int(input("Enter the value to insert at the end: "))
            Llist.insertatEnd(val)

        elif answer == "5":
            Llist.deleteatBegin()

        elif answer == "6":
                pos = int(input("Enter the position of the node to delete (0-based index): "))
                Llist.deleteatpos(pos)

        elif answer == "7":
                Llist.deleteatend()
        
        elif answer == "8":
                print("Current List: ")
                Llist.display()

        elif answer == "0":
            print("Exiting.\n")
            break

        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input. Enter numeric values")