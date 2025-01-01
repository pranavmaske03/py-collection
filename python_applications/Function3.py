
def fun():
    print("Inside fun ")

def Gun(No1,No2):
    return No1+No2,No1-No2,No1*No2

def Sun():
    print("Inside Sun")
    def Fun():
        print("Inside Fun of sun")
    Fun()

def main():
    fun()
    ret1,ret2,ret3 = Gun(10,5)
    print(ret1)
    print(ret2)
    print(ret3)
    Sun()


if __name__ == "__main__":
    main()