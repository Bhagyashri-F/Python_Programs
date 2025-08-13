def Display(No):
    i = 1
    
    while(i <= No):
        print("*", end = "\t")
        i = i + 1
        
    print("")  #in case of macOS to solve buffer related problem

def main():
    print("Enter the number : ")
    value = int(input())
    
    Display(value)

if __name__ == "__main__":
    main()