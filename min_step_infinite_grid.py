
def shortest_path(a,b):
    x = abs(a[0] - b[0])
    y = abs(a[1]-b[1])
    return max(x,y)
def coverpoints(sequence, size):
    count = 0
    for i in range(size-1):
        count+= shortest_path(sequence[i], sequence[i+1])
    return count




arr = [[0,0],[1,1],[1,2]]
ans = arr.zip
n = len(arr)
print(coverpoints(arr,n))
# k = shortest_path()



