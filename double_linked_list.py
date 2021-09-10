class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None




class Double_LinkedList:
    def __init__(self):
        #head is the lastest position in the ll where you enter the new node
        self.head = None
        #node to keep a copy of the first node for travesal purposes ( cant use head for this as it keeps mobing forward)
        self.headcopy = None

    def Push_at_start(self, data):
        #check if empty node
        if self.head == None:
            #this node becomes the head now (first node)
            self.head = Node(data)
        #No the first node, i.e, first node exists already
        else:
            #create the new node with curr data
            newnode = Node(data)
            #this new node will be inserted at beg, will have next as head
            newnode.next = self.head
            #curr head had prev as none but now will have this new ndoe as prev
            self.head.prev = newnode
            #now let the newnode pushed at beg be the head.
            self.head = newnode
            #for next push, this nserted new node will act as beg/head.
        print("pushed {} at the beg".format(data))

    def Push_at_end(self, data):
        #check if head exists ? bascially empty ll
        if self.head == None:
            self.head = Node(data)
            #store the copy of first node
            self.headcopy = self.head
        #Not the first item
        else:

            newnode = Node(data)
            #insert at the end of the head node
            self.head.next = newnode
            #newnode's prev will become head now
            newnode.prev = self.head
            #this new node will now be the head
            self.head = newnode
        print("pushed {} at the end".format(data))


    def traverse_backwards(self):
        #last node in the linked list
        curr_node = self.head
        #traverse backwards from this last node using prev pointer
        while curr_node!= None:
            print(curr_node.data)
            curr_node = curr_node.prev

    def traverse_forward(self):
        curr_node = self.headcopy
        while curr_node!=None:
            print(curr_node.data)
            curr_node = curr_node.next

    #driver code
if __name__ == '__main__':
    dll =  Double_LinkedList()
    dll.Push_at_end(10)
    dll.Push_at_end(20)
    dll.Push_at_end(30)
    dll.Push_at_end(30)
    print("----backwards----")
    dll.traverse_backwards()
    print("------forward -----")
    dll.traverse_forward()
