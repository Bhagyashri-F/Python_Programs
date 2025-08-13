def Division(No1, No2):
    Ans = 0
    Ans = No1 / No2
    
    return Ans

def main():
    print("Enter first number : ")
    value1 = int(input())
    
    print("Enter second number : ")
    value2 = int(input())
    
    iRet = Division(value1, value2)
    
    print(f"Division of {value1} and {value2} is {iRet}")

if __name__ == "__main__":
    main()