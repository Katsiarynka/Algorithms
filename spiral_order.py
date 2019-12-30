def spiral_order(A):
    if not A:
        return
    L, B = 0, 0
    T, R = len(A) - 1, len(A[0]) - 1 
    arr = [0] * (T+1)* (R+1)
    direction = 0
    counter = 0
    while L < R and B < T:
        if direction == 0:
            for i in range(L, R + 1):
                arr[counter] = A[L][i]
                counter += 1
            B += 1
            direction = 1
        elif direction == 1:
            for i in range(B, T + 1):
                arr[counter] = A[i][R]
                counter += 1
            R -= 1
            direction = 2
        elif direction == 2:
            for i in range(R, L - 1, -1):
                arr[counter] = A[T][i]
                counter += 1
            R -= 1
            direction = 3
        elif direction == 3:
            for i in range(T, B - 1, -1):
                arr[counter] = A[i][L]
                counter += 1
            L += 1
            direction = 0
    return arr
            

# doesn't work correctly
assert(spiral_order([[1,2],[3,4],[5,6]]) == [1, 2, 4, 6, 0, 0])
assert(spiral_order([[1,2,3],[4,5,6]]) == [1, 2, 3, 0, 0, 0])
assert(spiral_order([[1,2,3,4,5,6]]) == [0, 0, 0, 0, 0, 0])
assert(spiral_order([[1],[2],[3],[4],[5],[6]]) == [0, 0, 0, 0, 0, 0])
assert(spiral_order([]) == None)
