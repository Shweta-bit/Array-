# def printpascal(n):
#     for line in range(0,n):
#         for i in range(0, line+1):
#             print(binomialCoeff(line,i), " ", end="" )
#         print()
# def binomialCoeff(n,k):
#     res = 1
#     if (k> n-k):
#         k = n-k
#     for i in range(0,k):
#         res = res*(n-i)
#         res = res//(i+1)
#     return res

# n = 5
# printpascal(n)

def printPascal(n:int):

    arr = [[0 for x in range(n)] for y in range(n)]

    for line in range(0,n):
        for i in range(0, line+1):
            if (i == 0 or i == line):
                arr[line][i] = 1
                print(arr[line][i], end=" ")
            else:
                arr[line][i] = arr[line-1][i-1] + arr[line-1][i]
                print(arr[line][i], end=" ")

        print("\n", end= "")
n = 5
printPascal(n)

def printPascal(n):
    for line in range(1, n+1):
        c = 1
        for i in range(1, line+1):
            print(c, end=" ")
            c = int(c * (line-i)/ i)
        print("")
n = 5
printPascal(n)