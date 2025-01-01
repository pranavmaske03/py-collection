
class ArrayX:
    def __init__(self,size):
        self.Arr = list()
        self.size = size
    
    def Accept(self):
        print("Enter the elements of array :")
        no = 0

        for i in range(self.size):
            no = int(input())
            self.Arr.append(no)

    def Display(self):
        print("Elements of the array are :")
        for i in self.Arr:
            print(i,end="\t")
        print()
    
    def SearchFirstOcc(self,search):
        iCnt = 0
        iPos = -1

        for no in self.Arr:
            if no == search:
                iPos = iCnt
                break
            iCnt += 1
        return iPos
    


def main():
    size = 0
    value = 0

    print("Enter the size of the list :")
    size = int(input())

    obj = ArrayX(size)
    obj.Accept()
    obj.Display()

    print("Enter element to check in list :")
    value = int(input())

    ret = obj.SearchFirstOcc(value)
    if ret != -1:
        print("Element found at index : ",ret)
    else:
        print("There is no such element :")

if __name__ == "__main__":
    main()