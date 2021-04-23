def miniMaxSum(arr):
    sum = 0
    sums_list = []

    for int in arr:
        sum += int
        print(sum)

    for int in arr:
        sum -= int
        sums_list.append(sum)
        sum += int
    
    sums_list.sort()

    print(sums_list[0], sums_list[4])
    

    



arr = [7, 69, 2, 221, 8974]

miniMaxSum(arr)

# somo tudo
# crio uma lista vazia 
# pego a soma e num loop subtraio cada um dos elementos
# adiciono numa lista
# faco sort