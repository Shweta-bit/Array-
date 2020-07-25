# arrival = [1,3,5]
# departure = [2,6,10]
# k = 1
# aux_arr = []*max(departure)
# n = 0
# for i in arrival:
#     aux_arr.append(1)
# for j in departure:
#     aux_arr.append(0)
# print(aux_arr)


# 1 0 1 1 2 1 1 1 1 0
# # Python3 code for the above approach.
def HotelBooking(arrival, departure, n, k):

    count = []


    for i in range(0, n):
        count.append((arrival[i], 1))
        count.append((departure[i], 0))

    # Sort the vector
    count.sort()
    curr_book, max_book = 0, 0

    for i in range(0, len(count)):

        # If new arrival, increment current
        # guests count and update max active
        # guests so far
        if count[i][1] == 1:
            curr_book += 1
            max_book = max(max_book,
                             curr_book)
            if max_book > k:
                return False

        # if a guest departs, decrement
        # current guests count.
        else:
            curr_book -= 1


    # If max active guests at any instant
    # were more than the available rooms,
    # return false. Else return true.
    return True


# Driver Code
if __name__ == "__main__":

    arrival = [1, 2, 3, 4]
    departure = [10, 2, 6, 14]
    n = len(arrival)
    k = 4

    if HotelBooking(arrival,
                           departure, n, k):
        print("Yes")
    else:
        print("No")

    # This code is contributed by Rituraj Jain
