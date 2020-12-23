inp = "487912365"
arr = list(map(int, inp))
n = len(arr)
for i in range(100):
    pickup = [arr.pop(1) for x in range(3)]
    dest = arr[0]
    while dest in [arr[0]] + pickup:
        dest -= 1
        if dest == 0:
            dest = n
    dest = arr.index(dest) + 1
    arr = arr[:dest] + pickup + arr[dest:]
    arr = arr[1:] + [arr[0]]

ans = "".join([str(x) for x in arr])
one = ans.index("1")
print(f"Part 1: {ans[one+1:]}{ans[:one]}")

# Use a linked list, see: https://realpython.com/linked-lists-python/
# Use a dict to track Nodes: key is cup label, value is the Node that
# points to the next node.
class LinkedList:
    def __init__(self, nodes):
        self.n = len(nodes)
        self.nodes = {i: Node(i) for i in nodes}

        for i, j in zip(nodes, nodes[1:] + [nodes[0]]):
            self.nodes[i].next = self.nodes[j]

        self.head = self[nodes[0]]

    def __getitem__(self, i):
        return self.nodes[i]

    def __len__(self):
        return self.n


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


arr = list(map(int, inp))
arr.extend(range(len(arr) + 1, 1_000_000 + 1))
linked_list = LinkedList(arr)
cur = linked_list.head
for i in range(10_000_000):
    # Get next 3 nodes
    a = cur.next
    b = a.next
    c = b.next
    # Current label values
    dest = cur.data

    while dest in (cur.data, a.data, b.data, c.data):
        dest -= 1
        if dest == 0:
            dest = len(linked_list)

    # Lookup destination index
    dest = linked_list[dest]
    # Shuffle next values to move pickup
    cur.next = c.next
    cur = c.next
    c.next = dest.next
    dest.next = a

ans = linked_list[1].next.data * linked_list[1].next.next.data
print(f"Part 2: {ans}")
