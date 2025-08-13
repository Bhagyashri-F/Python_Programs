# Input : Rows : 4  
'''
   *
   *    *   
   *    *   *
   *    *   *   *  
'''

def Display(iRow):
    
    for i in range(1, iRow + 1, 1):
        print("*\t" * i)

def main():
    print("Enter number of Rows :")
    iValue = int(input())
    
    Display(iValue)
    
if __name__ == "__main__":
    main()