def miniMaxSum(arr):
    arr.sort()

    max_sum=0
    min_sum=0
    for i in range(len(arr)):
        if i!=0:
            max_sum+=arr[i]
        if i!=len(arr)-1:
            min_sum+=arr[i]

    print(min_sum, max_sum)
    


arr = [7, 69, 2, 221, 8974]
miniMaxSum(arr)
