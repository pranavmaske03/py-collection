
def Addition(*No):
    Ans = 0
    print(type(No))
    print(len(No))

    for i in No:
        Ans = Ans + i 
    
    return Ans

Result = Addition(11,22,33,44,55)
print(Result)

Result = Addition(11,22)
print(Result)

Result = Addition(11,22,33,)
print(Result)
