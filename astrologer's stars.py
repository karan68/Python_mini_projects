n=int(input("enter the no. of rows \t"))
s=bool(int(input("enter 1 for normal printing and 0 for reverse printing \t")))

if s:
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
else:
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
print("program ended--------------------------xxxxxxxxx-------------------------------")
