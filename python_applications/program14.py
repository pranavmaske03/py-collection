
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
    
    def Search(self,search):
        flag = False
        for icnt in self.Arr:
            if icnt == search:
                flag = True
                break
        return flag
        

def main():
    size = 0
    value = 0

    print("Enter size of the list :")
    size = int(input())

    obj = ArrayX(size)

    obj.Accept()
    obj.Display()
   
    print("Enter number to search in list :")
    value = int(input())

    bRet = obj.Search(value)
    if bRet == True:
        print("Element is present in list :")
    else:
        print("Element is not present in list :")


if __name__ == "__main__":
    main()