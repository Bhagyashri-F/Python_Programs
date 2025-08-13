class Demo:
    def __init__(self):
        print("Inside Constructor")
        
    def __del__(self):  # del method name(destructor)
        print("Inside Destructor")

def main():
    print("Inside main")
    
    obj1 = Demo()
    obj2 = Demo()
    
    del obj1   # del is keyword
    del obj2
    
    print("End of main")
    
if __name__ == "__main__":
    main()
    
    
# Inside main
# Inside Constructor
# Inside Constructor
# Inside Destructor
# Inside Destructor
# End of main