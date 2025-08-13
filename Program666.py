def StrUpr(data): 
    
    Output = ""  
    
    for ch in data:
        if(ch >= 'a' and ch <= 'z'):
            Output = Output + (ch - 32)  # ERROR - type casting not allowed (type conversion allowed)  
        else:
            Output = Output + ch
            
    return Output
                        
def main():
    print("Enter the String : ")
    str = input()
    
    strX = StrUpr(str)
    
    print(f"Updated string is : {strX}")
    
if __name__ == "__main__":
    main()