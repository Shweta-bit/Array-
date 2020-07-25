arrival = [1, 3, 5]
departure = [2, 6, 10]
n = len(arrival)
k = 1
ans=[]

def hotelBooking(arrival, departure, n, k):

    for i in range(n):
        ans.append((arrival[i], 1))
        ans.append((departure[i],0))

    ans.sort()

    curr_active= max_Active = 0

    for i in range(0, len(ans)):
        if  ans[i][1] == 1:
            curr_active += 1
            max_Active =max(max_Active,curr_active)

            if max_Active > k:
                return False
        else:
            curr_active -= 1
    return True
print(hotelBooking(arrival,departure,n,k))

