#!/usr/bin/env python
# coding: utf-8

# In[149]:


class node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        print("inside inti")
        self.head = None
        self.currnode = None
    
    def insert(self, val):
        newnode = node(val)
        if self.head == None:
            self.head = newnode
            self.currnode = self.head
        else:
            while(self.currnode.next!= None):
                self.currnode = self.currnode.next
            self.currnode.next = newnode
    
    def traverse(self):
        self.currnode = self.head
        while(self.currnode.next!= None):
            print("value  = ", self.currnode.data)
            self.currnode = self.currnode.next
        print("value  = ", self.currnode.data)
    
    def delete(self,value):

        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev:
                    
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
                    
            prev = curr
            curr = curr.next
            
        return False
        
    

        
            
            
            
    


# In[150]:


ll = LinkedList()

for i in range(10):
    ll.insert(i*2)
    
ll.traverse()


# In[153]:


ll.delete(18)
ll.traverse()


# In[ ]:



        
    
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




