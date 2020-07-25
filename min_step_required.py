# Python program to cover a sequence of points
# in minimum steps in a given order.

# function to give minimum steps to
# move from pop1 to p2
def shortestPath(p1, p2):

    # dx is total horizontal
    # distance to be covered
    dx = abs(p1[0] - p2[0])

    # dy is total vertical
    # distance to be covered
    dy = abs(p1[1] - p2[1])

    # required answer is
    # maximum of these two
    return max(dx, dy)

# Function to return the minimum steps
def coverPoints(sequence, size):

    stepCount = 0

    # finding steps for each
    # consecutive poin the sequence
    for i in range(size-1):

        stepCount += shortestPath(sequence[i],sequence[i + 1])

    return stepCount

# Driver code
# arr stores sequence of points
# that are to be visited
arr = [[4, 6] ,[ 1, 2 ], [ 4, 5] , [ 10, 12]]

n = len(arr)
print(coverPoints(arr, n))

# This code is contributed by shivanisinghss2110.
# x = abs(A[0]-A[1])
# y = abs(B[0]-B[1])
# return max(x,y)
#
# def pointstocover(arr,n):
#     n = len(arr)
#     count = 0
#     for i in range(n-1):
#         count += coverPoints(arr[i],arr[i+1])
# return count
