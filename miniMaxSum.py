def miniMaxSum(arr):
    arr.sort()
    max_sum = 0
    min_sum = 0
    sum = 0

    for int in arr:
        sum += int

    max_sum = sum - arr[0]
    min_sum = sum - arr[4]

    print(min_sum, max_sum)
    

    



arr = [7, 69, 2, 221, 8974]

miniMaxSum(arr)

# somo tudo
# crio uma lista vazia 
# pego a soma e num loop subtraio cada um dos elementos
# adiciono numa lista
# faco sort