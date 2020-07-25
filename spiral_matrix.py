def generateMatrix(n):
    if n <= 0:
        return []
    result = [[None for i in range(n)] for j in range(n)]
    left,right = 0,n-1
    top,bottom = 0,n-1
    current = 1
    while (left<= right and top<= bottom):
        for i in range(top,bottom+1):
            result[left][i] = current
            current += 1
        left += 1

        if (left > right):
            break
        for i in range(left,right+1):
            result[i][bottom] = current
            current += 1
        bottom -= 1

        if (bottom < top):
            break
        for i in range(bottom,top-1,-1):
            result[right][i] = current
            current += 1
        right -= 1
        if (right < left):
            break
        for i in range(right,left-1,-1):
            result[i][top] = current
            current += 1
        top += 1
        if (top > bottom):
            break
    return result

n = 3
print(generateMatrix(n))