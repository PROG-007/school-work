import os
while True:
    os.system("cls")
    inp=str(input("String Manipulator:\nA-Smallest Word\nB-Largest Word\nC-Ascending order of word length\nQ-Quit\n=>"))
    if len(inp)>1:
        print("Enter 1 character at once please!")
        os.system("PAUSE")
    elif inp.lower()=="a":
        a=str(input("Enter your sentence: "))
        min=len(a)
        minS=""
        for i in a.split():
            if len(i) < min:
                min=len(i)
                minS = i;
        print("Smallest word in the above sentence is- "+minS)
        os.system("PAUSE")
    elif inp.lower()=="b":
        a=str(input("Enter your sentence: "))
        max=0
        maxS=""
        for i in a.split():
            if len(i) > max:
                max=len(i)
                maxS = i;
        print("Longest word in the above sentence is- "+maxS)
        os.system("PAUSE")
    elif inp.lower()=="c":
        a=str(input("Enter your sentence: "))
        min,max=len(a),0
        ans=""
        for i in a.split():
            if len(i) < min:
                min=len(i)
                minS = i;
            if len(i) > max:
                max=len(i)
                maxS = i;
        for j in range(min,max+1):
            for i in a.split():
                if len(i) == j:
                    ans+=i+" "
        print("Your sentence in ascending order of characters in words is-\n"+ans)
        os.system("PAUSE")
    elif inp.lower()=="q":
        break
    else:
        print("I can't understand that invalid input, try again?")
        os.system("PAUSE")
os.system("PAUSE")
