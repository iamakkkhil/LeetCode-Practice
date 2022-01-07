def binary_problem(arr, N):

    # ----------------------------------------------------------------
    f = 0
    for x in range(1, N + 1):
        if x == 1:
            f+=0
            pass

        flag = 0
        for p in range(1, x):
            if arr[p-1] & arr[x-1]:
                flag = 1
                break
        
        if flag:
            for i in range(1, x+1):
                operation = arr[x-1] ^ arr[i-1]
                f += operation


    # ----------------------------------------------------------------
    g = 0
    for x in range(1, N + 1):
        if x == N:
            g+=0
            pass 

        flag_2 = 0
        for p in range(x+1, N+1):
            if arr[p-1] & arr[x-1]:
                flag_2 = 1
                break

        if flag_2:
            for i in range(x, N+1):
                operation = arr[x-1] ^ arr[i-1]
                g += operation

    return f+g
            


if __name__ == "__main__":
    print(binary_problem([2, 1, 2], 3))
    print(binary_problem([1, 2, 3], 3))
