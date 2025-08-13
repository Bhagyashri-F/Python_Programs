def CheckEvenOdd(No):
    if((No % 2) == 0):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    value = int(input())
     
    bRet = CheckEvenOdd(value)
    
    if(bRet == True):
        print(f"{value} is Even number")
        
    else:
        print(f"{value} is Odd number")

if __name__ == "__main__":
    main()