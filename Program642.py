def Minimum(Brr):
    iMin = Brr[0]
    
    for no in Brr:
        if(iMin > no):
            iMin = no
        
    return iMin

def main():
    print("Enter the number of elements")
    iLength = int(input())
    
    Arr = []
    
    print("Paese enter the elements : ")
    
    for i in range(1, iLength + 1):
        no = int(input())
        Arr.append(no)
        
    iRet = Minimum(Arr)
    print(f"Minimum element : {iRet}")
    
if __name__ == "__main__":
    main()