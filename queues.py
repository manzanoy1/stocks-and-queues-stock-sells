#Yanira Manzano
#3/25/2020

class QueueNode(object):

    def __init__(self, value, nxt, prv):
        self.value = value
        self.next = nxt
        self.prev = prv

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}:next={repr(nval)}:prev={repr(pval)}]"


class Queue(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def shift(self, obj):
        assert obj != None, "Cannot add None to queue."

        if self.head:
            node = QueueNode(obj, None, self.tail)
            # set tail.next to None
            self.tail.next = node
            # set tail to node
            self.tail = node
        else:
            self.head = QueueNode(obj, None, None)
            self.tail = self.head

    def unshift(self):
        if self.head:
            node = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = node.next
                self.head.prev = None
            return node.value
        else:
            return None

    def drop(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def first(self):
        return self.head != None and self.head.value or None

    def empty(self):
        return self.head == None

    def count(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def dump(self, mark='----'):
