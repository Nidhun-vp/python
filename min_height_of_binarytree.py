class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def MinHeight_tree(root):
    if(root==None):  
        return 0
    else:
        ldepth=MinHeight_tree(root.left)
        rdepth=MinHeight_tree(root.right)
        
        if(ldepth>rdepth):
            return(1+rdepth)
        else:
            return(1+ldepth)        
        
        



root =Node(1)
root.left=Node(2)     
root.right=Node(3)  
root.left.left=Node(4)     
root.left.right=Node(5) 
root.left.left.right=Node(7)     
root.right.right=Node(6)      

print("height of tree :",MinHeight_tree(root))   