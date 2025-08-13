def Replace(data):   
    Output = ""
    
    for ch in data:
        if(ch == 'a'):
            Output.append('_')  # ERROR - due to append
        else:
            Output.append(ch)
            
    return Output
            
def main():
    print("Enter the String : ")
    str = input()
    
    strX = Replace(str)
    
    print(f"Updated string is : {strX}")
    
if __name__ == "__main__":
    main()