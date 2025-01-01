# List datatype

# Heterogeneous
# Unordered
# Unindexed
# Immutable
# Duplicate not allowed

Arr = {11,22.22,True,"Marvellous",11}
Crr = (11,18.90,True,"Marvellous",11)
Brr = [11,13.24,True,"marvllous,",11]

print(Arr)
print(Brr)
print(Crr)
#print(Arr[0])

print(len(Arr))

Arr.add("python")
print(Arr)

print(len(Arr))

Arr.remove("python")
print(Arr)