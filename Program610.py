def CheckDivisible(No):
    if(((No % 3) == 0) and ((No % 5) == 0)):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    value = int(input())
     
    bRet = CheckDivisible(value)
    
    if(bRet == True):
        print(f"{value} is Divisible by 3 and 5")
        
    else:
        print(f"{value} is Divisible by 3 and/or 5")

if __name__ == "__main__":
    main()