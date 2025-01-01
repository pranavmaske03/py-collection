
class ArrayX:
    def __init__(self,size):
        self.Arr = list()
        self.size = size
    
    def Accept(self):
        print("Enter the elements of the list :")
        no = 0

        for i in range(self.size):
            no = int(input())
            self.Arr.append(no)
    
    def Display(self):
        print("Elements of the list are :")

        for i in self.Arr:
            print(i,end = "\t")
        print()

    def CountOdd(self):
        count = 0
        for i in self.Arr:
            if i % 2 != 0:
                count += 1
        return count

def main():
    size = 0
    ret = 0

    print("Enter the number of elements in list :")
    size = int(input())

    obj = ArrayX(size)
    obj.Accept()
    obj.Display()

    ret = obj.CountOdd()
    print(ret)
if __name__ == "__main__":
    main()