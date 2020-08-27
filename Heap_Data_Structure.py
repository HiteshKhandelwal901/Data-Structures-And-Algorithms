#!/usr/bin/env python
# coding: utf-8

# In[123]:


class HeapSort:
    
    def heapify(self,heap_tree, init, n):
        """
        arguments - heap_tree which is an array which needs some modification to be converted into max_heap
                  - init: intial node or value (root node) that is assumed to be largest
                  - n: length of heap_tree array
        
        """
        #intialize the root node as largest and left and right node according the formula ( l = 2i +1, r = 2i+2)
        largest = init
        left= 2*init+1
        right = 2*init+2
        
        #compare if the left and right child of current root node is greater than root, if true, change largest
        
        if left<n and heap_tree[init]<heap_tree[left]:
            largest = left
            
        if right<n and heap_tree[largest]<heap_tree[right]:
            largest = right
            
        #check if root is still the largest or if the largest  value has changed from init
        if largest!=init:
            #swap the current largest value with root(init)
            heap_tree[init], heap_tree[largest] = heap_tree[largest], heap_tree[init]
        #since left or right child is larger now ( indicated by chnage in largest value from init), heapify again with largest as root node
            self.heapify(heap_tree, largest, n )   
    


        
        
    def Build_maxHeap(self,heap_tree,n):
        """
        input - heap_tree which is an array a[a1,a2,a3,a4,..an] that needs to converted into max heap
        output - heap_tree which is an array a[a3,a1,a4,a7,..an] that follows the max heap property which is
        for i from 0 to len(array) - (a[i-1/2] > a[2i+1] and a[2i+2])
        n: length of heap_tree array
        """
        #loop through each root node ( all nodes except for leaf nodes) gievn by eq rootnode = i-1/2. then with each root node heapify()
        for i in range(n//2-1, -1, -1):
            self.heapify(heap_tree,i,n)
        #return heap_tree
    
    def extract(self,heap_tree):
        #swap elements 0, last and then heapify again by removing last elemenet ( in loop - n-1 to 0, n-2 to 0,... 0-0)
        for i in range(len(heap_tree)-1,0,-1):
            heap_tree[i], heap_tree[0] = heap_tree[0], heap_tree[i]
            #print("data after ", i , " || ", heap_tree)
            self.heapify(heap_tree, 0, i)
        #return heap_tree
            


    def heapsort(self,heap_tree):
        self.Build_maxHeap(heap_tree, len(heap_tree))
        self.extract(heap_tree)
        
        


# In[124]:


arr = [ 12, 11, 13, 5, 6, 7] 
h = HeapSort()
print(arr)


# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[119]:





# In[ ]:





# In[120]:





# In[ ]:




