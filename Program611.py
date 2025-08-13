def Maximum(No1, No2, No3):
    if((No1 > No2) and (No1 > No3)):
        return No1
    
    elif((No2 > No1) and (No2 > No3)):
        return No2    
    
    else:
        return No3

def main():
    print("Enter first number : ")
    value1 = int(input())
    
    print("Enter second number : ")
    value2 = int(input())
    
    print("Enter third number : ")
    value3 = int(input())
     
    iRet = Maximum(value1, value2, value2)
    
    print(f"{iRet} is Maximum")

if __name__ == "__main__":
    main()