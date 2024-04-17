from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class Cache:
    def __init__(self, capacity=None):
        self.capacity = capacity if capacity is not None else 3
        self.front = Node("F", 0)
        self.tail = Node("T", 0)

        self.front.next = self.tail
        self.tail.prev = self.front
        self.hmap = defaultdict(Node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if node.key in self.hmap:
            del self.hmap[node.key]

        return

    
    def insertNode(self, node):
        self.hmap[node.key] = node

        nextNode = self.front.next
        node.next = nextNode
        nextNode.prev = node
        node.prev = self.front
        self.front.next = node

    def get(self, key):
        if key not in self.hmap:
            return -1

        # whenever a key is fetched from cache, move it to the front
        node = self.hmap[key]
        self.removeNode(node)
        self.insertNode(node)
        return node.val

    def put(self, key, value):
        if key in self.hmap:
            self.removeNode(self.hmap[key])

        newNode = Node(key, value)
        self.hmap[key] = newNode
        self.insertNode(newNode)

        if len(self.hmap) >  self.capacity:
            print("[WARNING] CAPACITY EXCEEDED, REMOVING LRU with key: ", self.tail.prev.key)
            self.removeNode(self.tail.prev)

    def print(self):
        currentNode = self.front
        output = "F"
        while currentNode.next != self.tail:
            currentNode = currentNode.next
            output += f" <-> {currentNode.key}"
        output += " <-> T"
        print(output)
        
        for key, value in self.hmap.items():
            print("\tkey: {}, value: {}".format(key, value.val))

# obj = Cache()
# 
# x=3
# for i in range(x):
#     print("==> inserting node ", i)
#     obj.insertNode(Node(i, i+3))
# 
# print("==> printing cache")
# obj.print()
# 
# 
# print("==> get 1")
# print(obj.get(1))
# obj.print()
# 
# print("==> get 0")
# print(obj.get(0))
# obj.print()
# 
# print("==> get nonexisting")
# print(obj.get(123))
# obj.print()

