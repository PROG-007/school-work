x=str(input())
i = 0
while True:
    if x[-1:i:-1] == x[-1]:
        i+=1
        break
    else:
        i+=1
print(i+1)

#This code calculates the length of a string without any in-built functions, for loop, in and range operators, exception handling or modifying the inputed string
