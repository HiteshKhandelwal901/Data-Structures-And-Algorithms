from dataclasses import dataclass

@dataclass
class node:
    """
    node data structure conating node.left , node.right and the value of this node
    left and right are intialized to none and value is equal to none and is required
    during node creation
    
    """
    left  = None
    right = None
    #root  : None
    value : None
        
class BST:
    
    """
    Binary search tree with following operations
    
    - insert
    - search
    - delete
    - travesal
      - inorder
      - preorder
      - postorder
      
    """
    
    
    
    def invert_tree(self,root):
        if root == None:
            #print(root, " is leaf node")
            return 
        else:
            root.right, root.left = root.left, root.right
            self.invert_tree(root.left)
            self.invert_tree(root.right)
            
  #------------------------------- -----------------INSERT NODE BST-----------------------------------------------------------  
    def insert(self, root_node, node):
        
        """
        insert a node to the binary tree
        arguments:
        root_node - top most node to travese the tree and find the position to insert the node
        node - node to be inserted 
        
        """
        
        
        if root_node is None:
            root_node = node
        else:
            #check if node is present in left subtree or right subtree
            if node.value <= root_node.value:
                #if in left subtree, check if left child of the current root is empty or not
                if root_node.left is None:
                    #if empty then insert here
                    root_node.left = node
                else:
                    #if not empty then with this current node as a root node travese again
                    self.insert(root_node.left, node)
            else:
                #if node in right subtree, repeat the above same procedure
                if root_node.right is None:
                    root_node.right = node
                else:
                    self.insert(root_node.right, node)
                    
#--------------------------------------------INORDER TRAVS BST ----------------------------------------------------------------                  
   
    
    def inorder_travs(self,start_node):
        #if the node exists, then left, root, right
        if start_node: 
            
            self.inorder_travs(start_node.left) 
            
            print(start_node.value) 
            
            self.inorder_travs(start_node.right)

#--------------------------------------------PostOrder TRAVS BST ------------------------------------------            

    def Postorder_travs(root): 
        #if the node exists then left, right, root
        if root: 
            self.Postorder_travs(root.left) 
  
            self.Postorder_travs(root.right) 
   
            print(root.value)
    
 #--------------------------------------------PREORDER TRAVS BST ------------------------------------------   
    def preorder_travs(root):
        #if the node exists then left, right, root
        if root:
            
            print(root.value)
            
            self.preorder_trav(root.left)
            
            self.preorder_travs(root.right)
            
#----------------------------------------------Search BST-------------------------------------------------            
  
            
    def search(self, key, root):
        #if root is the key node or if root ===None ( leaf) then return root
        if root is None or root.value == key:
            return root
        else:
            #keep travesing left or right based on key
            if key < root.value:
                return self.search(key, root.left)
            else:
                return self.search(key, root.right)
            
##--------------------------------------------DELETE BST ------------------------------------------
            
    def delete(self, key, root):
        #if even after reaching the leaf node, key is not found then left.next( root) will be none and hence return
        if root is None:
            print(key, "does not exits")
            return root
        #keep travesing the tree based on key value to find the node
        else:
            
            if key < root.value:
                root.left = self.delete(key, root.left)
            elif key > root.value:
                root.right= self.delete(key, root.right)
            else:
                #one or zero child
                if root.right is  None:
                    temp = root.left
                    root = None
                    return temp
                    
                elif root.left is  None:
                    temp = root.right
                    root = None
                    return temp
                    
                else:
                    #two child
                    temp = inorder_successor(root.right)
                    root.key = temp.key
                    root.right = self.delete(root.right, temp.key)
        return root
                    

#--------------------------------------------RUNNING BST ------------------------------------------

A = [20,30,40,50,60,70,80]
root = node(A[0])
Bst = BST()
for i in range(1, len(A)):
    Bst.insert(root, node(A[i]))
print("------------- BST after all insertion ----------")
Bst.inorder_travs(root)
print("BST --- searching ---- ")
x = Bst.search(160, root)
print("x = ", x)
print("----- deleting-item --------------")
Bst.delete (30, root)
print("-----travesing BST ater deleting ----------")
Bst.inorder_travs(root)
