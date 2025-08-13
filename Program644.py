def CountEvenOdd(Brr):
    iCntEven = 0
    
    for no in Brr:
        if(no % 2 == 0):
            iCntEven += 1
        
    return iCntEven, len(Brr) - iCntEven

def main():
    print("Enter the number of elements")
    iLength = int(input())
    
    Arr = []
    
    print("Please enter the elements : ")
    
    for i in range(1, iLength + 1):
        no = int(input())
        Arr.append(no)
        
    iEven, iOdd = CountEvenOdd(Arr)
    print(f"Number of Even elements : {iEven}")
    print(f"Number of Odd elements : {iOdd}")
    
if __name__ == "__main__":
    main()