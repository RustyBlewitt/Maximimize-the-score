from math import floor

class priority_q:
    def __init__(self):
        self.nodes = []

    def get_parent_index(self, child_index):
        if(child_index == 0):
            print("Already at root")
            raise IndexError("Trying to access parent of root")

        # Plus and minus one are adjustments for zero first indexing.
        return floor( (child_index + 1) / 2) - 1

    def get_left_child(self, parent):
        return ( (parent + 1) * 2 ) - 1

    def get_right_child(self, parent):
        return (parent + 1) * 2

    def heapify_up(self):
        child = len(self.nodes) - 1
        parent = self.get_parent_index(child)

        while(self.nodes[child] > self.nodes[parent]):
            temp = self.nodes[parent]
            self.nodes[parent] = self.nodes[child]
            self.nodes[child] = temp
            child = parent
            if child == 0:
                break
            parent = self.get_parent_index(child)

    def heapify_down(self):
        parent = 0
        left_child = self.get_left_child(parent)
        right_child = self.get_right_child(parent)

        while(1):
            if left_child >= len(self.nodes):         # If left child doesn't exist
                break

            elif right_child >= len(self.nodes):       # If right child doesn't exist
                max_child = left_child

            else:
                max_child = left_child if self.nodes[left_child] > self.nodes[right_child] else right_child

            if self.nodes[max_child] > self.nodes[parent]:
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[max_child]
                self.nodes[max_child] = temp

                parent = max_child
                left_child = self.get_left_child(parent)
                right_child = self.get_right_child(parent)
                
            else:
                break

    def show_heap(self):

        next_level = 2
        levels = []
        line = ''

        for i in range(len(self.nodes)):
            if i == next_level - 1:
                levels.append(line)
                line = ""
                next_level *= 2
            line += ' ' + str(self.nodes[i])

            if i == len(self.nodes)-1:
                levels.append(line)

        for l in levels:
            print(l.center(30))

    def enqueue(self, n):
        self.nodes.append(n)
        if len(self.nodes) > 1:
            self.heapify_up()

    def dequeue(self):
        root = self.nodes[0]
        self.nodes[0] = self.nodes.pop()
        self.heapify_down()
        return root