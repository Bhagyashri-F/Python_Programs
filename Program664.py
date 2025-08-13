def Replace(data):   
    
    i = 0
        
    for i in range(len(data)):
        if(data[i] == 'a'):
            data[i] = '_'   # ERROR - As String in Python is immutable
                        
def main():
    print("Enter the String : ")
    str = input()
    
    Replace(str)
    
    print(f"Updated string is : {str}")
    
if __name__ == "__main__":
    main()