import sys

def Addition(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])
    Result = Addition(value1,value2)
    print(Result)


if __name__ == "__main__":
    main()