
Cube = lambda no : no * no * no
Square = lambda no : no**2

def main(): 
    Ret = Cube(5)
    print("Cube is : ",Ret)

    Ret = Square(5)
    print("Square is : ",Ret)

if __name__ == "__main__":
    main()