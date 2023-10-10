import os
from ut import color

os.chdir(os.path.dirname(os.path.abspath(__file__)))
paths=["example1.cpp","example2.cpp","generator.py"]
for i in paths:
    if not os.path.exists(i):
        print(color("r",f"not found {i} file, please make sure it exists in the same path"))
        exit(1)

statusE1done=False
statusE2done=False


while True:
    if not os.path.exists("example1.exe"):
        print(color("p","compiling example1.cpp..."))
        os.system(f"g++ example1.cpp -o example1")
        if not os.path.exists("example1.exe"):
            print(color("y","example1 fail in compilation, select 'c' to continue or any other to end: "))
            res=input()
            if(res!='c'):
                exit(0)
        with open("status.txt","w") as f:
            with open("example1.cpp","r") as g:
                f.write(f"{g.readlines()}\n")
            with open("example2.cpp","r") as g:
                f.write(f"{g.readlines()}")
        break

    if not os.path.exists("example2.exe"):
        print(color("p","compiling example2.cpp..."))
        os.system(f"g++ example2.cpp -o example2")
        if not os.path.exists("example2.exe"):
            print(color("y","example2 fail in compilation, select 'c' to continue or any other to end: "))
            res=input()
            if(res!='c'):
                exit(0)
        with open("status.txt","w") as f:
            with open("example1.cpp","r") as g:
                f.write(f"{g.readlines()}\n")
            with open("example2.cpp","r") as g:
                f.write(f"{g.readlines()}")
        break

    with open("status.txt","r") as f:
        with open("example1.cpp") as g:
            if(f"{f.readline()[:-1]}"==f"{g.readlines()}"):
                statusE1done=True
        with open("example2.cpp") as g:
            if(f"{f.readline()}"==f"{g.readlines()}"):
                statusE2done=True

    if statusE1done:
        res=input("example1 already compiled, compile again? press 'y' to compile or any other to continue: ")
        if res=="y":
            statusE1done=False

    if not statusE1done:
        print(color("p","compiling example1.cpp..."))
        os.remove("example1.exe")
        os.system(f"g++ example1.cpp -o example1")
        if not os.path.exists("example1.exe"):
            print(color("y","example1 fail in compilation, select 'c' to continue or any other to end: "))
            res=input()
            if(res!='c'):
                exit(0)

    if statusE2done:
        res=input("example2 already compiled, compile again? press 'y' to compile or any other to continue: ")
        if res=="y":
            statusE2done=False

    if not statusE2done:
        print(color("p","compiling example2.cpp..."))
        os.remove("example2.exe")
        os.system(f"g++ example2.cpp -o example2")
        if not os.path.exists("example2.exe"):
            print(color("y","example2 fail in compilation, select 'c' to continue or any other to end: "))
            res=input()
            if(res!='c'):
                exit(0)

    with open("status.txt","w") as f:
        with open("example1.cpp","r") as g:
            f.write(f"{g.readlines()}\n")
        with open("example2.cpp","r") as g:
            f.write(f"{g.readlines()}")

    print(color("g","done"))
    break
            


cases=int(input("number of cases to solve: "))
print()
def getInputA():
    global xa
    global a
    xa+=1
    if(xa<len(a)):
        return a[xa]
    else:
        print(color("r","overflow read file"))
        exit(1)
def getInputB():
    global xb
    global b
    xb+=1
    if(xb<len(b)):
        return b[xb]
    else:
        print(color("r","overflow read file"))
        exit(1)

import generator
for j in range(1,cases+1):
    generator.run("inputTest.txt")
    print(color("p",f"Case No.{j} generated"))
    xa=xb=-1
    os.system("example1 < inputTest.txt > output1.txt")
    print(color("c",f"example_1 - case {j}: done"))
    os.system("example2 < inputTest.txt > output2.txt")
    print(color("b",f"example_2 - case {j}: done"))
    with open(f"output1.txt",'r') as f:
        a=f.readlines()
        for i in range(len(a)):
            if a[i][-1]=='\n':
                a[i]=a[i][:-1]

    with open(f"output2.txt",'r') as f:
        b=f.readlines()
        for i in range(len(b)):
            if b[i][-1]=='\n':
                b[i]=b[i][:-1]
    
    ex=True
    for i in range(min(len(a),len(b))):
        if(getInputA()!=getInputB()):
            print(color("r",f"Diferece in line:{i+1} | diference:(example 1) {a[i]} ||(example 2) {b[i]}"))
            ex=False
            for i in range(max(len(a),len(b))):
                print(f"{i+1}| {a[i]}\t\t{b[i]}")
            break
    if not ex:
        print("\n")
        with open("inputTest.txt","r") as f:
            for i in f.readlines():
                print(i,end="")
        break
    if(ex and len(a)!=len(b)):
        print(color("r",f"Diferece in line:{min(len(a),len(b))} | not equal size:(example 1) {a[min(len(a),len(b))]} ||(example 2) {b[min(len(a),len(b))]}"))
    elif ex:
        print(color("g",f"done case:{j}"))
    print()
    