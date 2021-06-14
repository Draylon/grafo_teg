

class MQueue:
    def __init__(self):
        self.list = DLinkedList()
    def push(self,data):
        return self.list.push_back(data)
    def pop(self):
        return self.list.pop_front()
    def has(self,data):
        return self.list.find(data)
    def not_empty(self):
        if self.list.head != None:
            return True
        return False


class NodeLL:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self,data):
        curr = self.head
        while curr != None:
            if curr.data == data:
                return True
            curr=curr.next

    def push_front(self, data):
        NewNode = NodeLL(data)
        NewNode.next = self.head
        self.head = NewNode
        if self.tail == None:
            self.tail = NewNode

    def push_back(self, data):
        NewNode = NodeLL(data)
        NewNode.prev=self.tail
        if self.tail:
            self.tail.next=NewNode
        self.tail=NewNode
        if not self.head:
            self.head=NewNode
		
    def pop_front(self):
        if self.head:
            new_head = self.head.next
            retr = self.head
            if self.head == self.tail:
                self.tail=new_head
            self.head=new_head
            return retr.data

    def pop_back(self):
        if self.tail:
            retr=self.tail
            ntail = self.tail.prev
            ntail.next=None
            if self.tail == self.head:
                self.head=ntail
            self.tail=ntail
            return retr.data

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next



if __name__ == "__main__":
    llist = DLinkedList()
    llist.push_back("Mon")
    llist.push_back("Tue")
    llist.push_back("Wed")
    llist.push_back("Thu")
    print(llist.pop_front())
    print(llist.pop_back())
    llist.LListprint()