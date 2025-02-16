class Trees:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    root = Trees(5)

    branch1 = Trees(10)
    branch1.add_child(Trees(20))
    branch1.add_child(Trees(30))
    branch1.add_child(Trees(40))

    branch2 = Trees(15)
    branch2.add_child(Trees(25))
    branch2.add_child(Trees(35))
    branch2.add_child(Trees(45))

    root.add_child(branch1)
    root.add_child(branch2)

    return root

if __name__ == "__main__":
    root = build_tree()
    print(root.data)
    for child in root.children:
        print(child.data)
        for grandchild in child.children:
            print(grandchild.data)
            for grandgrandchild in grandchild.children:
                print(grandgrandchild.data)

