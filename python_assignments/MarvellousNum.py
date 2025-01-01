
def checkPrime(No):
    iCnt = 0
    flag = True

    for iCnt in range(2,int(No/2)+1):
        if(No % iCnt == 0):
            flag = False
            break
            
    if(flag == True):
        return True
    else:
        return False