class Demo:
    def __init__(self):
        print("Inside Constructor")
        
    def __del__(self):  # del method name(destructor)
        print("Inside Destructor")

def main():
    print("Inside main")
    
    obj1 = Demo()
    obj2 = Demo()
    
    print("End of main")
    
if __name__ == "__main__":
    main()
    
    
# Inside main
# Inside Constructor
# Inside Constructor
# End of main
# Inside Destructor
# Inside Destructor
