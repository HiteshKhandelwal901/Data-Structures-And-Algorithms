#!/usr/bin/env python
# coding: utf-8

# In[54]:


class MergeSort:
    
    def sort(self, array):

        if len(array)>1:
            
            mid   = len(array)//2
            left  = array[:mid]
            right = array[mid:]
            
            
            
            self.sort(left)
            self.sort(right)
            
            
            
            Ptr1 = 0
            Ptr2 = 0
            Ptr3 = 0
            
            
            
            while Ptr1<len(left) and Ptr2<len(right):
                
                if left[Ptr1] < right[Ptr2]:
                    array[Ptr3] = left[Ptr1]
                    Ptr1 += 1
                    
                else:
                    array[Ptr3] = right[Ptr2]
                    Ptr2 += 1
                
                Ptr3  += 1
                
            while Ptr1<len(left):
                array[Ptr3] = left[Ptr1]
                Ptr1 += 1
                Ptr3 += 1
                
            while Ptr2<len(right):
                array[Ptr3] = right[Ptr2]
                Ptr2 += 1
                Ptr3 += 1
                
        


# In[55]:


mergesort = MergeSort()
myArray = [20,10,15,7]


# In[56]:


mergesort.sort(myArray)
print(myArray)


# In[ ]:




