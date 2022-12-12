#This code will output the list in ascending order of the digits the nesed tuples include......(1,2,3,123) = 6 digits
# Q16 of my monday test in class 11 second term 2022 xD

a=[(1,2,3,765),(1,2),(234,345,456)]
b=[0]*len(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        b[i] += len(str(a[i][j]))
# print(a)
# print(b)
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
            a[j], a[j+1] = a[j+1], a[j]
# print()
print(a)
# print(b)
