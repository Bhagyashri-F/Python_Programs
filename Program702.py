class Node:
    def __init__(self, No):
        self.data = No
        self.next = None
        
##############################################################################################
##############################################################################################
        
class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

##############################################################################################
        
    def InsertFirst(self, No):
        newn = Node(No)
        
        if(self.first == None):     # LL is empty
            self.first = newn
            
        else:                       # LL contains atleast one node
            newn.next = self.first
            self.first = newn
            
        self.iCount += 1
            
##############################################################################################

    def InsertLast(self, No):
        newn = Node(No)
        
        if(self.first == None):     # LL is empty
            self.first = newn
            
        else:                       # LL contains atleast one node
            temp = self.first
            
            while(temp.next != None):
                temp = temp.next
                
            temp.next = newn
            
        self.iCount += 1
            
##############################################################################################
    
    def Display(self):
        temp = self.first
        
        while(temp != None):
            print(f"| {temp.data} | -> ", end = "")
            temp = temp .next
            
        print("None")
    
##############################################################################################

    def Count(self):
        return self.iCount
    
##############################################################################################

    def DeleteFirst(self):
        if(self.first == None):
            return
        
        else:
            temp = self.first
            self.first = self.first.next
            
            del temp
            
            self.iCount -= 1
            
##############################################################################################

    def DeleteLast(self):
        if(self.first == None):     # LL is Empty
            return
        
        elif(self.first.next == None):                     # LL contains one node
            del self.first
            self.first = None
                    
        else:                       # LL contains more than one node
            temp = self.first
            
            while(temp.next.next != None):
                temp = temp.next
                
            del temp.next
            
            temp.next = None
            
        self.iCount -= 1
        
##############################################################################################

    def InsertAtPos(self, No, Pos):
        if((Pos > self.iCount + 1) or (Pos < 1)):
            return
        
        elif(Pos == 1):
            self.InsertFirst(No)
            
        elif(Pos == self.iCount + 1):
            self.InsertLast(No)
            
        else:
            newn = Node(No)
            
            temp = self.first
            
            for i in range(1,Pos - 1, 1):
                temp = temp.next
                
            newn.next = temp.next
            temp.next = newn
            
            self.iCount += 1
    
##############################################################################################
##############################################################################################

def main():
    print("Demonstration of Singly Linear Linked List")
    
    sobj = SinglyLL()
    
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    
    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
    sobj.Display()
    
    iRet = sobj.Count()
    print(f"Number of nodes in Linked List are : {iRet}")
    
    sobj.InsertAtPos(105 , 5)
    
    sobj.Display()
    
    iRet = sobj.Count()
    print(f"Number of nodes in Linked List are : {iRet}")
    
##############################################################################################
    
if __name__ == '__main__':
    main()