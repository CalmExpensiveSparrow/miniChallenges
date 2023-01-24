
class Single:
    def __init__(self, saved_data:str, next_node=None):
        self.saved_data = saved_data
        self.next_node = next_node


    def reverse_list(self):
        reversed_list = []
        this_node = self
        while this_node.next_node is not None:
            reversed_current = this_node.next_node
            reversed_next = this_node

            reversed_node = Single(reversed_current, reversed_next)
            reversed_list.append(reversed_node)

            this_node = this_node.next_node
        print(reversed_list[node.saved_data] for node in reversed_list)

single3 = Single("yellow")
single2 = Single("blue", single3)
single1 = Single("red", single2)

single1.reverse_list()








# single = Single()
# single.reverse_list()


class Double:

    def __init__(self, this_list, next=None, prev=None):
        self.this_list = this_list
        self.next = next
        self.prev = prev