import threading

def DisplayEven():
    val = 21
    print("Even number are :")
    for i in range(1,val):
        if i % 2 == 0:
            print(i)
   
def DisplayOdd():
    val = 21
    print("Odd numbers are :")
    for i in range(1,val):
        if i % 2 != 0:
            print(i)     


def main():

    even = threading.Thread(target = DisplayEven,args = ())
    odd = threading.Thread(target = DisplayOdd)

    even.start()
    odd.start()

if __name__ == "__main__":
    main()