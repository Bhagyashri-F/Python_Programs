def Maximum(Brr):
    iMax = Brr[0]
    
    for no in Brr:
        if(iMax < no):
            iMax = no
        
    return iMax

def main():
    print("Enter the number of elements")
    iLength = int(input())
    
    Arr = []
    
    print("Paese enter the elements : ")
    
    for i in range(1, iLength + 1):
        no = int(input())
        Arr.append(no)
        
    iRet = Maximum(Arr)
    print(f"Maximum element : {iRet}")
    
if __name__ == "__main__":
    main()