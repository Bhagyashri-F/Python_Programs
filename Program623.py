def Factorial(No):
    iFact = 1
    
    for i in range(1, No + 1):
        iFact = iFact * i
        
    return iFact

def main():
    print("Enter the number : ")
    value = int(input())
    
    iRet = 0
    
    iRet = Factorial(value)
    
    print(f"Factorial is : {iRet}")

if __name__ == "__main__":
    main()