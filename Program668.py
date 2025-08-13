def StrUpr(data): 
    
    Output = ""  
    
    for ch in data:
        if(ch >= 'a' and ch <= 'z'):
            Output = Output + chr(ord(ch) - 32)  # converting character(ch) to ASCII ,, again converting it to character using chr
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