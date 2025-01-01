
class ArrayX:
    def __init__(self,size):
        self.Arr = list()
        self.size = size
    
    def Accept(self):
        print("Enter the elements of list :")
        no = 0

        for i in range(self.size):
            no = int(input())
            self.Arr.append(no)
    
    def Display(self):
        print("Elements of the list are :")
        for i in self.Arr:
            print(i,end = "\t")
        print()
    
    def CountEven(self):
        count = 0
        for no in self.Arr:
            if no % 2 == 0:
                count += 1
        return count

def main():
    size = 0

    print("Enter size of the list :")
    size = int(input())

    obj = ArrayX(size)

    obj.Accept()
    obj.Display()
    ret = obj.CountEven()
    print("Count of the even elements is : ",ret)


if __name__ == "__main__":
    main()