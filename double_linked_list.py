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
            #print("empty")
            #this node becomes the head now (first node)
            self.head = Node(data)
            self.headcopy = self.head
            #print("self.head = ", self.head.data)
        #No the first node, i.e, first node exists already
        else:
            #create the new node with curr data
            newnode = Node(data)
            #print("newnode = ", newnode.data)
            #this new node will be inserted at beg, will have next as head
            newnode.next = self.head
            #print("newnode.next = ",newnode.next.data)
            #curr head had prev as none but now will have this new ndoe as prev
            self.head.prev = newnode
            #print("self.head.prev = ", self.head.prev.data)
            #now let the newnode pushed at beg be the head.
            self.head = newnode
            #print("self.head  = ", self.head.data)
            #for next push, this nserted new node will act as beg/head.

        print("pushed {} at the beg".format(data))
        #print(self.head.data)

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

   #traverse in the order of First in First  out.
    def FIFO(self, insertion_id):
        #id =1 => 10->20->30->40 (hc = 10, h = 40). id = 2 => 40->30->20->10 (hc = 10, h = 40).
        curr_node = self.headcopy
        #if id = 1, then move forward from headcopy
        if insertion_id == 1:
            while(curr_node!=None):
                print(curr_node.data)
                curr_node = curr_node.next
        #if id!=1 move backword from headcopy
        else:
            while(curr_node!=None):
                print(curr_node.data)
                curr_node = curr_node.prev


    # in order of last in first out
    def LIFO(self, insertion_id):
        #now from the abive example we start from head and move from there
        curr_node = self.head
        #if id =1 move bacwards from head
        if insertion_id == 1:
            while(curr_node!=None):
                print(curr_node.data)
                curr_node = curr_node.prev
        #if id!=1 move forward from there
        else:
            while(curr_node!=None):
                print(curr_node.data)
                curr_node = curr_node.next



    #driver code
if __name__ == '__main__':
    dll_start =  Double_LinkedList()
    dll_end  = Double_LinkedList()
    dll.Push_at_start(10)
    dll.Push_at_start(20)
    dll.Push_at_start(30)
    dll.Push_at_start(30)
    print("----FIFO----")
    dll_start.FIFO(2)
    print("------LIFO -----")
    dll_start.LIFO(2)

    dll_end.Push_at_end(10)
    dll_end.Push_at_end(20)
    dll_end.Push_at_end(30)
    dll_end.Push_at_end(40)
    dll_end.FIFO(1)
    dll_start.LIFO(2)
