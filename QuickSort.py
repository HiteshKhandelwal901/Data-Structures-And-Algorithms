#!/usr/bin/env python
# coding: utf-8

# In[62]:


class QuickSort:
    
    
        def sort(self, data, low, high):
            """
             Arguments : 
             
             data -- unsirted data that needs to be sorted
             low -- first index of data
             high -- last index of data
           
             Step 1 -- put the pivot element in its correct position by calling partition. 
             Step 2 -- use the pivot returend pivot index by partition() to sort recussively 
                      sort subarray left to pivot indx and right to pivot index by partioning them further
            
             returns none
            """
            
            if low < high:
                #pivot element = data[high], put this element into right position and partiton the array (in-pace)
                p_index = self.partition(data, low, high)
                #recussively create left and right for each returned left and right arrays above
                self.sort(data, low, p_index-1)
                self.sort(data, p_index+1, high)
            return 0
    
        
        def partition(self,data, low, high):
            """
            Arguments:
            data - unsorted array in which we need to put the pivot element in correct position
                   and partition data into left and right arounf pivot index
            low  - first index of data
            high - last index of data
            
            """
            #intialize data[low] to be pivot element and low to be pivot index
            pivot_element  = data[high]
            pivot_idx = low
            #loop over the entire data
            for j in range(low,high):
                #for each data at J check if  data[j] is lesser than current pivot element
                if data[j] < pivot_element:
                    #if true then, swap the data present at Jth index with data present at current pivot_index
                    data[j], data[pivot_idx] = data[pivot_idx], data[j]
                    #update/increment the pivot index
                    pivot_idx = pivot_idx + 1
            #At the end of one loop/pass swap the pivot element with the data present at current pivot index 

            data[pivot_idx], data[high] = data[high], data[pivot_idx]
            return pivot_idx
    
    
if __name__ == "__main__": 
    Q = QuickSort()
    data = [102,30,401,111,73,104,101]
    high = len(data)-1
    Q.sort(data, 0, high)
    print(" sorted array = ", data)  


# 

# In[ ]:





# In[61]:



    


# In[ ]:





# In[ ]:





# In[ ]:




