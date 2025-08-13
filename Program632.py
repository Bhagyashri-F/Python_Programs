# Accept numbers and display factors

def SumFactors(iNo):
    iSum = 0
    
    for i in range(1, (iNo // 2) + 1):
        if(iNo % i == 0):
            iSum += i
    
    return iSum

def main():
    print("Enter the Number :")
    iValue = int(input())
    
    iRet = SumFactors(iValue)
    
    print(f"Summation of factors of {iValue} is {iRet}")
    
if __name__ == "__main__":
    main()